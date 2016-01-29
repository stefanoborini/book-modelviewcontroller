# Proxy Model

-----------
**Note**: In the context of Qt MVC, a Proxy Model is a Model Pipe design.
Django also defines a Proxy Model concept, but it is unrelated to the one 
expressed here: the application of the Proxy design pattern to a Model object.

-----------

### Motivation

We want to access an external resource, such as one provided by an HTTP 
server or a database. Proxy Model encapsulate the logic needed to access 
the remote service, specifically:

- Issue the request to the remote service
- Handle error conditions
- Convert received data into a representation useful for the client code.

Additionally, the Proxy Model can:

- Throttle an excessive number of requests in a short amount of time
- Cache obtained results and manage the cache expiration
- Observe the remote service for changes, for example through
  polling on a secondary thread.

### Design

The design of a Proxy Model is generally dependent on the service it 
represents. Interfaces are designed to comply with the abstraction of the
remote service. When the client code asks for data, the Model issues the 
appropriate request to the service provider. Client code is generally 
unaware of the exact nature of the backend exposed by the Proxy Model.

When the Model implements SQL access to a specific database table, the resulting
Proxy Model is normally called **Table Data Gateway**. An instance of this Model
represents the backend database Table as a whole, not a specific row, and its 
methods provide access to CRUD operations.

### Practical example: Django Models

A simple Django Model provides an example of a Proxy Model.

```
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

For the class definition given above, Django's internals create a SQL table 
whose columns are defined by the class properties (`first_name` and `last_name`). 
Instances of the `Person` class are represented as table rows. 

The Person class can be instantiated, stored in the database, modified, or 
used to retrieve an already present instance. 

```python
person = Person(first_name="A.", last_name="Einstein")
person.save()

person.first_name = "Albert"
person.save()

another_person = Person.objects.get(last_name="Galilei")
```

Under the hood, the Django Model implementation converts the operations into SQL statements.

### Practical example: Thrift services

Another example of Proxy Model is provided by Thrift, a cross-language Remote Procedure Call
framework. An Interface Definition Language specifies the interface of the remote service

```idl
service Calculator {
   i32 add(1:i32 num1, 2:i32 num2),
}
```

which is compiled into python to produce the following code

```python
class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def add(self, num1, num2):
    """
    Parameters:
     - num1
     - num2
    """
    self.send_add(num1, num2)
    return self.recv_add()

  def send_add(self, num1, num2):
    self._oprot.writeMessageBegin('add', TMessageType.CALL, self._seqid)
    args = add_args()
    args.num1 = num1
    args.num2 = num2
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_add(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = add_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "add failed: unknown result")
```

The above Proxy handles the complexity of the network exchange, providing a simple interface to 
client code

```python
result = client.add(3, 4)
```

### References

- Martin Fowler, "Patterns of Enterprise Application Architecture". Addison-Wesley, 2003.
- Django - https://www.djangoproject.com/
- Apache Thrift - https://thrift.apache.org/

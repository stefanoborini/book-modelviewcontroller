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

- issue the request to the remote service
- handle error conditions
- convert received data into a representation useful for the client code.

Additionally, the Proxy Model can:

- Throttle an excessive number of requests in a short amount of time
- Cache obtained results and manage the cache expiration
- Observe the remote service for changes, for example through
  polling on a secondary thread.

### Design

The design of a Proxy Model is generally dependent on the service it 
represents. Interfaces are designed to comply with the abstraction of the
remote service. When the client code asks for data, the Model issues the 
appropriate request to the service provider.

### Practical example

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

Under the hood, Django Model implementation converts the operations into SQL statements.

# Transactional Setting

### Motivation

Your Model has multiple settable attributes, each one listened independently by
Views. You want to change the Model state, and the logic needs to do so
requires to set many of these attributes. Every set operation would trigger a
notification. The behavior would be

1. Set A attribute on the Model
2. Views are notified of change
3. Set B attribute on the Model
4. Views are notified of change  
  
During step 2, listeners will be notified of the change and sync against a
Model where only one of the attributes has been changed. Depending on the
specific details of your Model and Views, this state may be inconsistent or not
representable by the Views. However, setting and notification of the individual 
attributes may still be needed for specific use cases.

What is needed is to trigger notification when all set operations have been 
performed

1. Set A silently
2. Set B silently
3. Notify change

### Design

Transactional setting is the most trivial strategy to achieve 
the result outlined in the Motivation, the others being using a 
Lazy Model or an Accumulator. 

Transactional setting implements a setter function accepting both
attributes. This setter function alters the object state and then
issues the change notification.

### Practical Example

A Model representing a network connection to a remote host
might want to present functionality to change the host, the port,
and both simultaneously. If any listener is in charge of initiating a
network connection, the notification should be delivered only when the 
Model contains correct host information.

```python
class Connection(Model):
    def setHost(self, host):
        self._host = host
        self.notifyListeners()

    def setPort(self, port)
        self._port = port
        self.notifyListeners()

    def setHostAndPort(self, host, port):
        self._host = host
        self._port = port
        self.notifyListeners()
```

Without the `setHostAndPort()` method, reconnecting from `http://one.example.com:80` to
`http://two.example.com:8080` would either trigger a rogue connection to 
`http://one.example.com:8080` (when `setPort(8080)` is called) or to 
`http://two.example.com:80/` (when `setHost("two.example.com")` is called).

Note how the `setHostAndPort()` method cannot, for obvious reasons, call the 
independent setters, but must reimplement the setting logic. If this logic is complex,
it might be good practice to factor it out in a separate "silent setter" method.

### Variation 1: qualified notification

If the Model performs qualified notification, the behavior in absence of transactional setting
will be

1. Set A attribute on the Model
2. Views are notified of A change
3. Set B attribute on the Model
4. Views are notified of B change

Transactional setting will provide a method performing the following sequence:

1. Set A attribute on the Model
2. Set B attribute on the Model
3. Views are notified of A change
4. Views are notified of B change

or if the qualification protocol allows to deliver information about multiple
changes at once

1. Set A attribute on the Model
2. Set B attribute on the Model
3. Views are notified of A+B change

### Variation 2: set/add multiple items

Transactional setting can also be used to add multiple elements at once, generally for a 
Model behaving as a list. The Model might want to implement an interface for adding
both one or multiple elements. The implementation normally acts as a syntactic sugar to
generate a list with one item.

```python
class BookCollection(Model):
    def addBook(self, book):
        self.addBooks([book])

    def addBooks(books):
        self._books.extend(books)
        self.notifyListeners()
``` 

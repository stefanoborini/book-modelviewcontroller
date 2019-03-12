---
grand_parent: MVC Variations
parent: Variations on the Model
nav_order: 15
summary: Setting multiple attributes at once with late notification.
---
# Transactional Setting

### Motivation

Your Model has multiple settable attributes, each one listened independently by
Views. The business logic requires setting two or more attributes to reach the desired final
Model state. Each set operation triggers a notification, as shown:

  1. Set A attribute on the Model
  2. Views are notified of change
  3. Set B attribute on the Model
  4. Views are notified of change

During step 2, listeners will be notified of the change and sync against a
Model where only one of the attributes has been changed. Depending on the
specific details of your Model and Views, this state may be inconsistent or not
representable by the Views. However, setting and notification of the individual 
attributes may still be needed for specific use cases.

The desired goal is to trigger notification only when all set operations have been 
performed, as follows:

1. Set A attribute without notification
2. Set B attribute without notification
3. Views are notified of change

### Design

Transactional setting is the most trivial strategy to achieve 
the result outlined in the Motivation, the others being using a 
Lazy Model or an Accumulator, examined later.

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
    def set_host(self, host):
        self._host = host
        self.notify_listeners()

    def set_port(self, port):
        self._port = port
        self.notify_listeners()

    def set_host_and_port(self, host, port):
        self._host = host
        self._port = port
        self.notify_listeners()
```

Without the ``set_host_and_port()`` method, reconnecting from ``http://one.example.com:80`` 
to ``http://two.example.com:8080`` would either trigger a rogue connection to 
``http://one.example.com:8080`` (when ``set_port(8080)`` is called) or to 
``http://two.example.com:80/`` (when ``set_host("two.example.com")`` is called).

For obvious reasons, the ``set_host_and_port()`` cannot reuse the independent setters, and must
therefore reimplement the setting logic. If this logic is complex, it might be good practice to 
factor it out in a separate "silent setter" method.

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
    def add_book(self, book):
        self.add_books([book])

    def add_books(books):
        self._books.extend(books)
        self.notify_listeners()
``` 

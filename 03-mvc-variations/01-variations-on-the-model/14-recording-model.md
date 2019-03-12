---
grand_parent: MVC Variations
parent: Variations on the Model
nav_order: 14
summary: Record the changes for later consumption.
---
# Recording Model

### Motivation

A Recording Model maintains a log of the changes occurred to its state.
This information can then be used by external client code, for example to 
perform a refresh only if the visualized information was changed, or to 
perform undo.

This technique carries the liability of forgetting to clear the log,
leading to memory exhaustion.

### Practical Example

The following example shows a Model class that records changes to its properties

```python
class Customer(Model):
    def __init__(self):
        self._changes = { 
            "name": [],
            "surname": [],
            "address": []
        }
        self._name = None
        self._surname = None
        self._address = None

    def set_name(self, name):
        old_name = self._name
        self._name = name
        self._changes["name"].append((old_name, name))
        self.notify_listeners()

    # <similar code for set_surname/set_address
   
    def changes(self, property_name):
        return self._changes[property_name]
    
    def clear_changes():
        for changes in self._changes.values():
            del changes[:]
```

The setters record the changes in the ``self._changes`` dictionary. Performing the following operation

```python
c = Customer()
c.set_name("Rob")
c.set_name("Robert")
```

will produce a ``self._changes["name"]`` list containing two elements: the first transition ``(None, "Rob")``,
and the second transition ``("Rob", "Robert")``.

### Variation: record the sequence of changes

The solution given above does not record if, for example, the surname was changed before or after the name. 
An alternative implementation can store this information by e.g. using a list instead of a dictionary
for ``self._changes``.

```python
class Customer(Model):
    def __init__(self):
        self._changes = []
        # <...>

    def set_name(self, name):
        # <...>
        self._changes.append(("name", old_name, name))
        # <...>

    def changes(self):
        return self._changes
```

### Variation: interest only in the last change

The log length can be limited, potentially to a single change, by simply
replacing the previous change information with the latest.  This approach also
removes the liability of forgetting to clear the log.

```python
class Customer(Model):
    de f __init__(self):
        self._last_change = None
        # <...>

    def set_name(self, name):
        # <...>
        self._last_change = ("name", old_name, name)
        # <...>

    def last_change(self):
        return self._last_change
```

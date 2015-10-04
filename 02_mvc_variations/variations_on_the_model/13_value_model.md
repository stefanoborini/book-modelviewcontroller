# Value Model

### Motivation

A Value Model is a model class adapting a complex Model into 
a single value, exposed thought a uniform and trivial interface:
a getter ``ValueModel.value()``, a setter ``ValueModel.setValue()``, 
and notification. 

Views and Controllers can be extremely simple and off-the-shelf,
as they only interact with the Value Model's generic and minimalist 
interface. They can disregard the nature of the adapted Model, 
leaving to the Value Model the responsibility to take care of the details.

### Design

The ValueModel class acts as an adapter

<p align="center">
    <img src="images/value_model/value_model.png" width=200 />
</p>

A trivial implementation of a ValueModel would be:

```python
class ValueModel(Model):
    def __init__(self, model_object):
        self._model_object = model_object
    
    def setValue(self, value):
        # do potentially complex logic on self._model_object
        # to appropriately manipulate the passed value
        # This method triggers a valueChanged notification.
        
    def value(self):
        # do potentially complex logic on self._model_object
        # to extract a single value
    
```

Many different ValueModel classes can be implemented, each one
adapting a different SubModel, or operating over different parts of a SubModel.
Views and Controllers interact with the ValueModels through the minimalist interface, and are therefore agnostic of the ValueModel used.

### Practical Example

One could adapt an ``Customer`` object through two ValueModels: ``NameValueModel`` and ``SurnameValueModel``. 

```python
class NameValueModel(Model):
    def __init__(self, customer):
        self._customer = customer
    
    def setValue(self, value):
        self._customer.name = value
        self.notifyObservers()
        
    def value(self):
        return self._customer.name
        
class SurnameValueModel(Model):
    def __init__(self, customer):
        self._customer = customer
    
    def setValue(self, value):
        self._customer.surname = value
        self.notifyObservers()
        
    def value(self):
        return self._customer.surname
```

Each of these two ValueModels can use an off-the-shelf 
``StringWidget`` View, agnostic of the actual nature of the ``Customer`` model and retrieving/modifying data through the ValueModel interface.


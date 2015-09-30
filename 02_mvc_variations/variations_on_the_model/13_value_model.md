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

# Design

The ValueModel class acts as an adapter

<p align="center">
    <img src="images/value_model/value_model.png" width=200 />
</p>

Many different ValueModel classes can be implemented, each one
adapting a different SubModel, or operating over different parts of a SubModel.
Views and Controllers interact with the ValueModels through the minimalist interface, and are therefore agnostic of the ValueModel used.

### Example 

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

This mechanism can be extended to alter any particular and potentially complex 
aspect of an object to a trivial interface defining a value. For example, one
could define a ValueModel to accept a string containing a street address.
The ValueModel could parse the string, lookup the street address according to
the parsed information, obtain a canonical format of the address according
to the city directory, and associate it to the current object.


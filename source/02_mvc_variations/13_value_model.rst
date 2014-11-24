Value Model
-----------

A Value Model is a technique to render a complex Model object or Model behavior
into a uniform and trivial interface, containing a getter, a setter, and
notification services::

    class ValueModel(Model):
        def __init__(self, model_object):
            self._model_object = model_object
        
        def value(self):
            # do potentially complex logic on self._model_object
            # to extract a single value
        
        def setValue(self, value):
            # do potentially complex logic on self._model_object
            # to appropriately manipulate the passed value
            # This method triggers a valueChanged notification.


This mechanism can be extended to alter any particular and potentially complex 
aspect of an object to a trivial interface defining a value. For example, one
could define a ValueModel to accept a string containing an street address.
The ValueModel could parse the string, lookup the street address according to
the parsed information, obtain a canonical format of the address according
to the city directory, and associate it to the current object.

The concept behind the Value Model is that View and Controller can only deal
with a generic, minimalist ``value/setValue()`` interface, disregarding the
underlying nature of the passed object, and leaving the specific ValueModel to
take care of the details.
 

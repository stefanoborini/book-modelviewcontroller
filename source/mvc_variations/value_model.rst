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


The concept behind the Value Model is that View and Controller can only deal
with a generic, minimalist ``value/setValue()`` interface, disregarding the
underlying nature of the passed object, and leaving the specific ValueModel to
take care of the details.
 

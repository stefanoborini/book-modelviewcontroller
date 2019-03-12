---
grand_parent: MVC Variations
parent: Variations on the View
nav_order: 1
summary: Client code injects data extraction logic in the View's at initialization.  
---
# Pluggable View

-----

Note: In the context of the Web framework Flask, Pluggable View refers to a different concept.

-----

### Motivation

For some applications, different Views may have the same implementation for 
the UI part, but different implementation for data extraction from the Model.
To prevent duplication, two strategies has already been analysed:

1. implement the common UI logic in a base View class, and have subclasses 
   reimplementing the data extraction logic.
2. use a Value Model, which puts the extraction logic on a Model adapter object, 
   transforming the Model's complex interface into a trivial getter/setter pair. 
   The resulting View is agnostic of the nature of the Model and the complexity 
   of the extraction logic.

In this section, we present the **Pluggable View** design. An adaptor function
is defined, and injected into the View at initialization. The model is processed
through this function to obtain the data to be displayed.

### Design

The View accepts a function object containing the data extraction logic. This
function receives the Model object and returns the relevant data needed by the
View.

```python
def extractor(model):
    return str(model.get_value())

view = View(model, extractor)
```

The View listens to the Model for change notifications. When a change occurs,
the View calls the function object, passing the Model and obtaining the relevant
information as a return value.

```python
class View:
    # <...>
    def notify(self):
        value = self.extractor(self.model)
        self.set_value(value)
```

Variations of this solution allow for multiple functions to extract 
different parts of the Model, or the possibility to swap the function 
object after construction. More elaborate extractors can return 
"UI decorated" information, such as returning both the value and the text 
color to use.

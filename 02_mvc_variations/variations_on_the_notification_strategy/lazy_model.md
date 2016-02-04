<!--- Done -->
# Lazy Model

### Motivation

A Lazy Model is an intermediate solution between Active and Passive Model 
that retains centrality of the notification bookkeeping, but delegates 
notification triggering. It is a good strategy to retain full control on the
notification flow as in the Passive model, but at the same time keep 
the listeners' list centralized so that they can all be notified of the 
changes, no matter which Controller performs them. 

With the resulting design, the Controller is free to perform multiple 
changes on the Model object, and trigger the notification when done.

### Design

Like an Active solution, listeners register on the Model and await for
notification; Differently from it, methods that modify the Model do not call
``Model.notify_listeners()``. Instead, the Controller issues the call.

<p align="center">
    <img src="images/lazy_model/lazy_model.png" />
</p>

### Practical example 

A trivial example of Controller code using a Lazy Model notification strategy
would behave as follows

```python
class Controller():
    def perform_operation(self):
        model = self.model
        
        # None of these setters trigger notification.
        model.set_name("Enrico")
        model.set_surname("Fermi")
        model.set_nationality("Italian")

        # Views are notified of the changes here.
        model.notify_listeners()
``` 

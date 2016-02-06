# Passive Model

### Motivation

Traditional MVC uses the so-called **Active Model**: when the Model changes
its listeners are notified of the change. 

The Active Model strategy has a counterpart in the **Passive Model**. A Passive
Model does not perform notification services. Instead, this task is
performed by the Controller.

Passive Model has its area of excellence in Web-based MVC, where the
fundamental nature of the HTTP protocol prevents the Model to 
notify the View. 

### Design

The interaction diagram shows the behavior of a Passive Model

<p align="center">
    <img src="images/passive_model/passive_model.png" />
</p>

Specifically, the sequence of events is:

1. The Controller modifies the Model
2. The Controller informs the View to update itself
3. The View now inquires the Model contents as in the Active case.

The major shortcoming of a Passive Model is that Views get desynchronized
if multiple Controllers can modify the Model. Collaboration between Controllers
can prevent this desynchronization, but for all practical purposes an Active
Model quickly becomes a better solution. If this is required, a Passive Model
can become Active either through inheritance or by using a wrapper class
satisfying the Passive Model's original interface. This wrapper will receive
change requests from Controllers, delegate them to the Passive Model, and
finally notify the listeners. 

Despite the disadvantage, the Passive Model has the following important advantages: 

- Any object (e.g. a key-value dictionary, a list, a single value, a previously
  developed business object) can be used as a Model without modifications
- It allows better control on the refresh of the View. The Controller
  can issue multiple changes to the Model without triggering a View's refresh 
  for each change
- As commented in the Motivation section, Web-based MVC cannot use an 
  Active Model strategy due to the intrinsic separation of Models from 
  rendered Views.

### References

- [MSDN documentation: Model-View-Controller](https://msdn.microsoft.com/en-us/library/ff649643.aspx)

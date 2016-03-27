# Vetoers

### Motivation

A Vetoer is a special Model listener that provides pluggable, encapsulated 
validation of Model changes. When a Model content needs to change,
the Vetoers are inquired first. If any Vetoer denies the change, the Model
keeps the old state and discards the change request.

### Design

A Model supporting Vetoing must provide a separate listener collection for Vetoers
and a dedicated interface to register and deregister them.

When the Model is requested to change, the vetoers' `modelAboutToChange()`
method is called first, passing the new intended value. Vetoers evaluate the 
proposed change and respond with an Accept/Deny, either by returning
an appropriate value, or raising an exception.  The Model aborts the change if
one Vetoer respond with a Deny. If, on the other hand, all vetoers approve the
change, then the Model state is changed accordingly and listeners are notified.

### Design Variation: Fixup value

In a more flexible design, Vetoers may also return an alternative
value that the Model can use as a compliant substitute. The proposed
value is then passed to the remaining vetoers and, if accepted, applied to the
Model's state.

### Design Variation: Vetoers in the View

The Qt Toolkit presents an alternative solution for Vetoing at the View
level: Qt Validators. A Validator plugs into a widgets and examines the widget's
content for validity, rejecting any user event that would bring the widget's
content in an invalid state.

The drawback of Validators is that business rules are more naturally enforced
at the Model level. While convenient, Qt Validators misplace the validation
logic, potentially allowing invalid data to get into the Model through other 
routes or an incorrectly configured Validator.

### Practical example: JavaBean constrained properties

An example of this mechanism is the "constrained property" in javabeans.  


### References

- [Java VetoableChangeSupport](http://docs.oracle.com/javase/7/docs/api/java/beans/VetoableChangeSupport.html)
- [Java constrained properties](https://docs.oracle.com/javase/tutorial/javabeans/writing/properties.html)
- [Qt Validators](http://doc.qt.io/qt-4.8/qvalidator.html)


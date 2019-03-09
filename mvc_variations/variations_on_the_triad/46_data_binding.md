---
parent: Variations on the triad
---
# Data binding

### Motivation

We want to reduce boilerplate code to synchronize changes the bidirectional
communication between the Model and the View.

The Model is a one-to-one representation of the View widgets. Changes in the content
of the Model immediately propagates to the widget, and vice-versa, changes in the 
Widget are immediately propagated to the Model.

The code is declarative.

Validation is possible, but only for individual values. The Model can inform the View
that the value is incorrect and raise an exception. This is interpreted by the View by
coloring the cell red, for example.

synchronization can also be one-directional.
Diretionality is important if we want to elimate coercion problems.

Data binding basically connects specific widgets with specific model attributes through 
a trivial, off the shelf controller that is invisible to us.

Possibility to say how to transform the data as they go back and forth.
Backbone.js stickit onSet/onGet

The triad becomes a 1:1 connection between view and model, with the controller
being invisible and generic.

### Practical Examples

Cocoa Bindings, TraitsUI

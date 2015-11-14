# Key Value Observer

### Motivation

A form of qualified notification where every change in property of an object
is delivered to its listeners with the qualification of the name of
the changed property, and the object whose property changed. The listener
receives this notification through a single method.

### Practical Example

Used in Apple Cocoa. Main problem is that the qualification model now requires to
check the changed property against a string, which is prone to typos.
Setters are now basically open to injection of code from outside.


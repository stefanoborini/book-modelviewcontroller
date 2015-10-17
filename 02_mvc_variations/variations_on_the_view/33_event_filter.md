# Event Filter

### Motivation

An Event Filter is a special kind of Controller that intercepts UI events 
before they are delivered to the View. The gained additional flexibility
allows to handle specific events differently than the standard response
provided by the View, or to suppress some events so that they never reach
the View.

### Design

Event Filters are generally objects with a specific interface or function objects.
They can be connected to Model objects, and act directly on their interfaces.
Views supporting Event Filters provide an interface to set (and unset) them. The View
must be designed so that the event routing is first attempted toward the Event Filter, 
if any.

Events are routed into the Filter by the View, through a `handle_event(event)` interface.
The Event Filter can now recognize a specific event and perform operations on the
Models it is connected to. These Models may or may not be the same that the View is 
observing.

If the Event Filter handles the Event, the latter is generally not propagated further.
The View is notified of this through either a flag on the Event class or a boolean 
return value for the `handle_event()` method.

As a consequence of its design and purpose, the Event Filter must be dependent on
the UI, and must know how to handle UI events. 


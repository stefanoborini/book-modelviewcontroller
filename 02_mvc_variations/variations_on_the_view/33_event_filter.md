# Event Filter

### Motivation

An Event Filter is a special kind of Controller that intercepts UI events 
before they are delivered to the View. The gained additional flexibility
allows to handle specific events differently than the standard response
provided by the View, or to suppress some events so that they never reach
the View.

### Design

Event Filters can be either objects with a specific interface, or function objects 
with a signature accepting the event. They can be connected to Model objects, and 
act directly on their interfaces.

Views supporting Event Filters provide an interface to set (and unset) them. The View
must be designed so that the event routing is first attempted toward the Event Filter, 
if any.

<p align="center">
    <img src="images/event_filter/event_filter.png">
</p>

From the activity diagram, events are routed into the Filter by the View, through a `handle_event(event)` interface.
The Event Filter can now recognize a specific event and perform operations on the
Models it is connected to. These Models may or may not be the same that the View is 
observing.

If the Event Filter handles the Event, 
The View is notified of this through either a flag on the Event class or a boolean 
return value for the `handle_event()` method. The event is not handled further.

If the Event Filter call instead returns False, the View handles the Event as usual.
The Event Filter may decide to return False even if it actually handles the event, to 
let the View perform its operation as well. This may be an indication of a technical smell,
but it might be justified if, for example, the Event Filter performs event logging for debugging purposes.

As a consequence of its design and purpose, the Event Filter must be dependent on
the UI, and must know how to handle the UI Event interface. 

### Practical Example

The Qt toolkit offers a clear example of an Event Filter. Qt Objects have an `installEventFilter()` method. Any Qt QObject can be used as an Event Filter by reimplementing its `eventFilter()` method, whose signature consists of the View object and the event. 
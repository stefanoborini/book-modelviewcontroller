Notes
=====

change in a model is not the only reason why a view must inquire the model for data. 
The view may have to repaint itself after a show event.

the notification mechanism basically allow to inject code in setters.

Local models, or one global model?

the view should be able to query or inform the controller for action (will, should, did): delegate


Compare OSX bindings with MVVM ? Same stuff?
FIXME: relationship with apple, where the view is replaced with the child controller ?


All intralayer communication can only be routed through controller-controller connection. This connection is bidirectional.



following the hierarchic composition of the GUI nesting. The model can be the
same. In pratice, the scheme given above can be simplified by assuming a given
hierarchy talks to the same model In J2EE, this approach is also known as
Composite View.[11] [PIC of an example of a hierarchy with real widgets]




Keep networks simple and close.

Order of notification can have unexpected consequences on the state of your program.


keep your views able to deal with missing model or invalid data.

-

FIXME: pluggable view is overloaded as a term. Detail.

Naturally evolving toward a more declarative style

define your models as having atomic operations, be careful of uncontrolled notifications.


Problem with double notification if one notification is a subset of another.
e.g. contentChanged/lineMetaChanged and contentChanged/lineAdded. How to handle
the double notification? Pass an "event id" in the signal so that the client 
realizes that it's the same change that delivers two messages?




Typical situation
atapplication startup, a communication network is created.
the event loop takes control, in the main thread. 
Every time there's an event, the event loop dispatches that event. 
This in turn triggers changes that obey the static network and the
dynamic network through either direct calls or indirect (notification)
calls. During the whole cascade, the application is frozen until control
is returned to the event loop.

Separate threads can act independently, produced by code running in the main
(event loop) thread. The problem is that any change they can do can propagate 
through the network, and touch parts of the code that is currently handled by the 
main thread. As a result, the generally better way of handling this situation is
that secondary threads communicate with the main thread in two ways:
- setting state (using locks for synchronization)
- posting events into the event loop, so that the main thread can handle them.


Once an event is triggered, the application has around 1/60th of a second to return
control to the event loop, meaning that the object/notification network traversal
must be over quickly. If any event triggers something that can potentially last for more
than the mentioned amount of time, it must be executed in a separate thread, or the
interface responsiveness will suffer.
Having a separate thread carries its additional quirks: can't normally touch ui code,
must be synchronized.

Notes
=====


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


FIXME: MVC Notifications are always considered to be synchronous. They invoke methods directly
and wait for them to return.


Typical situation
atapplication startup, a communication network is created.
the event loop takes control, in the main thread. 
Every time there's an event, the event loop dispatches that event. 
This in turn triggers changes that obey the static network and the
dynamic network through either direct calls or indirect (notification)
calls. During the whole cascade, the application is frozen until control
is returned to the event loop.


Distinguish between Notifications (that are synchronous calls using the observer pattern) 
vs events (that instead are dispatched through the event loop)


With signals, you might have to adapt the signals that your model emits
to the specific needs of your views. 
A coarse grained signal that forces
a heavy refresh on the view may be better split into a separate signal
specific to the area of the model that actually affects the view. In 
practice, the model communication pattern may have to adapt to the View's
implementation details to guarantee responsiveness.

For example, if you have a view displaying the number of lines in a document,
subscribing to a contentChanged signal may require a recalculation of the number
of lines at every character inserted. It may make sense to provide a lineNumberChanged
signal, so that line number display is updated only when the model actually
performs a change in the total number of lines.


Some toolkit and libraries allow you to define the network dynamically.
Other allow you to define the network statically. The network cannot be changed.


How to handle null values.


### Practical Example: Monitoring file contents

A Model that represents the contents of a file is unable to trigger any notification if
changes from an external source are performed in the file. [^1]
the Model can be implemented so that the Controller occasionally requests (e.g. with a timer) 
to verify if changed occurred. When such changes are found, the Controller can act
to update the View. Alternatively, the Model can perform notification to the listening Views
as in an Active Model 


- or by having an Active Model that uses a secondary thread to monitor for changes in the file, and issues notification
when such changes are found


unless an appropriate implementation handles 

[^1] In this discussion, we ignore the problem to obtain a consistent state while reading a potentially incomplete file.


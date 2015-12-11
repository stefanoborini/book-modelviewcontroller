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


# Qualified Notification Model

### Motivation


### Design


Inform the View about which model actually changed Prevent a View refresh if
the model changes on some information that is not displayed due to the state of
the view Inform the View of what actually changed, instead of asking for a full
refreshes


The Model can send messages qualified with a subject, so to inform the views of
what kind of change has occurred. OR parametrize the notify method to deliver
information about the change the model has.  Either the View register itself
and lists which messages it is interested in (and only if this matches, the
message is delivered) or it gets all messages and acts only on those who it is
interested in. Alternatively, fragment the Model into two model objects, so
that the View can connect only to the part that is relevant.

To prevent excessive refreshes with multiple changes: pass a flag to update(),
or accumulate changes on the view side and refresh only after a given amount of
time has passed, or add to a queue the changes, then consume the queue until no
more changes are needed, then force visual refresh.  notify() gets called with
a qualified flag, the previous value and the new value.

notify() gets called with a qualified flag specifying which change has occurred
, the previous value and the next value

The view subscribes to specific events from the model, and 
receives notifications only when those events actually occur.

case: Model changes, but not in the data relevat to the view.

notify can say, for example, what value is changing, the value before and after.

A model can also pass a data update object to the listeners, and the view can react
to that update object, instead of resyncing against the new model state.

can't a view fetch information from multiple models, and deliver signals to different controllers having different roles?

A View can depend on different Models, but this requires the View to know which Model is delivering the notification.
Add a note on the fact that if the model pushes information, then this information characteristics falls on the signature of the notifyObserver() methods. So, its signature must be somehow generic. The model pretends to know what the view is specifically interested in, something it might not know, so it must simply send itself, and let the view go through it, or have a protocol to specify what changed.

Drawback: you may end up implementing a protocol in the notify() method.

The view does not inquire the model through an interface.
The model is closed to that. it just produces events with
a data change object, and synchronizes through that.

Advantages: 
 - the data update object may contain logic on how to present itself on the views, especially if this rendering is trivial (e.g. pure text)
 - if the model is on another thread, it pushes and forces the refresh of the view. In the traditional case, the view may lag behind.

Disadvantages:
 - transfer stuff that may be useless for that specific view. The view may then subscribe for specific data and receive only those in the data update object



you can send a changeset object through the signal, with a well defined interface
for the type and change content


If you want to retain control over the notification in order to 
prevent trashing, you can use a passive model and let the controller do the notification
once it has performed the modifying action.

Useful to tell the observers which part has actually changed.

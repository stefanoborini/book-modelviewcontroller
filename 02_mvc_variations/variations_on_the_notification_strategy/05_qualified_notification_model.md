# Qualified Notification Model

### Motivation

The most basic form of Model notification just informs the listeners that 
a change occurred in its state. Views must now retrieve the new state and
repaint themselves. This approach is simple, but it might be too coarse 
and wasteful. Consider these scenarios:

- A specific View is only interested in a subset of the Model. 
  The Model changes, but not in the data relevant to the View.
  The View is now forced to repaint even if none of the data
  it displays actually changed.

- A View has additional state which is destroyed by a full repaint.
  For example, a TreeView representing files in a directory keeps state 
  for the opened/closed sub-branches. If a new file is added and the View
  is forced to rescan and repaint, the open/closed state is discarded.

- A View takes a very long time to perform a repaint from the full
  model's content, but it can run faster if it operates only on the
  change.

These cases demonstrate how an unqualified notification can be wasteful
or damage the quality of the user interaction.

A Qualified Notification is a possible solution to the above
scenarios. It enhances the notification system with a more fine grained
protocol carrying information about what has changed in the Model. 

### Design

Qualified Notification is implemented by passing arguments to ``notify()``. method to deliver
information about the change the model has.  

notify() gets called with a qualified flag specifying which change has occurred
, the previous value and the new value
notify can say, for example, what value is changing, the value before and after.

View gets all messages and acts only on those who it is
interested in. 


### Additional comments


Alternatively, fragment the Model into two model objects, so
that the View can connect only to the part that is relevant.

Inform the View of what actually changed, instead of asking for a full
refreshes


To prevent excessive refreshes with multiple changes: pass a flag to update(),
or accumulate changes on the view side and refresh only after a given amount of
time has passed, or add to a queue the changes, then consume the queue until no
more changes are needed, then force visual refresh.  



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
prevent trashing, you can use a passive model and let the controller do the notification once it has performed the modifying action.


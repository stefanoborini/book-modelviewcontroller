Model-View notification decoupling
----------------------------------

**Addressed Need:**

A problem carried over from the traditional MVC approach is the dependency of
the Model toward the views for notification purposes. When the model changes,
there's a need for the views to know this change occurred, but can we devise a
strategy to prevent the model to know about the views? The answer is to
decouple the dependency through a notification system, acting as an
intermediate between models and views. With a notification system, we
substitute the model dependency against the View with a dependency against the
notification system. Qt is an example of such strategy in place: a basic
strategy for Model objects is to make them derived classes of QObject. This Qt
core object provides “fire and forget” notifications to the Model: Qt signals.
The model does not need to know who is interested in these signals, and the
bookkeeping and invocation of the listeners' methods (Qt slots) is performed by
the notification system.  The clear advantage is that the notification system
is not a GUI object, allowing the Model to be tested without involving the GUI.
The model is also allowed to have multiple notification signals for different
conditions. Implementing the same with the traditional MVC approach would imply
FIXME
With a notification system, interested views are notified of the occurred
changes in the model, so they can update their state against the Model. 

With the model not knowing details about the other roles, with the exception of
a vague interface, there's no requirement for the model to understand special
semantics that are not his concern, such as the “GUI talk” that the View uses.
The model simply provides services about its state. it does not request
services to the other roles.  If needed, this data can eventually be persisted
and retrieved from external storage, like a file on the disk or a database. We
will examine design strategies for persistence later in this document.


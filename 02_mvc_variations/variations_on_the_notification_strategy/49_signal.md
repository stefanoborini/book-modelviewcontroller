# Signals

### Motivation

A Signal aggregates the notification logic as a separate object. 
Listeners register onto the signal instance. The Model triggers
the signal via an emit() method.

You can have multiple signals, creating multiple notification queues.
Each listener can subscribe to the signal they are interested in.

With signals, you might have to adapt the signals that your model emits
to the specific needs of your views. A coarse grained signal that forces
a heavy refresh on the view may be better split into a separate signal
specific to the area of the model that actually affects the view. In 
practice, the model communication pattern may have to adapt to the View's
implementation details to guarantee responsiveness.

For example, if you have a view displaying the number of lines in a document,
subscribing to a contentChanged signal may require a recalculation of the number
of lines at every character inserted. It may make sense to provide a lineNumberChanged
signal, so that line number display is updated only when the model actually
performs a change in the total number of lines.

A basic signal implementation just delivers the message to the listeners.
However, merging the approach from lazy model, a better signal class could implement three
strategies:

- open: the message is delivered as soon as triggered.
- closed: the message is not delivered and is ignored
- hold and release: the message is not delivered, but it is retained for later. 

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


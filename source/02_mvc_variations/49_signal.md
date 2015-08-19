Signals
-------

A signal extracts the notification logic in a separate object. 
Listeners register onto the signal instance. The model triggers
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


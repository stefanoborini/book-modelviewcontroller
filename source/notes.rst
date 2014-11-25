Notes
=====
Questions and Answers
Should I use a simple container approach (e.g. key/value dictionary with notifications as a model?
A simple container like a key/value dictionary can technically be used as a model, but as the amount of stored data grows, its unstructured nature and access will lead to entangled, inconsistent and undocumented storage. The model will be a “big bag of data” with very little clarity or enforced consistency. Enforcing access through well defined object relations and interfaces is recommended for models beyond the most trivial cases. 
Local models, or one global model?
case: Model changes, but not in the data relevat to the view.
Who performs validation? View? Controller? Model?
Consistency of the data inside the model?
How to report errors in the view?



the view should be able to query or inform the controller for action (will, should, did): delegate


Depending on the application, the model can host invalid data (that is, invalid for the application)

Compare OSX bindings with MVVM ? Same stuff?
You might have to fight your toolkit because it prefers a specific implementation of MVC
FIXME: relationship with apple, where the view is replaced with the child controller ?


All intralayer communication can only be routed through controller-controller connection. This connection is bidirectional.


The same data is present in the visual component in the GUI, in the Model
object, and finally in any backend the Model object may be using to access the
data, for example a SQL database. 

This can be reduced to two if we assume the Model to always query the database,
but it is wasteful. A better strategy is to cache the information in-memory.





completely unrelated. It must go somewhere else.

    When the view is shown, it will have to update its content. However, if the
    view is not visible, it should not receive events, so it should either
    unsubscribe from the model when hidden, or mute the delivery by first checking
    if it's visible before proceeding to update itself. The reason is that if a
    view is connected to the model, and this view requires time to refresh itself,
    we don't want to trigger this refresh if the view is not visible to the user.






following the hierarchic composition of the GUI nesting. The model can be the
same. In pratice, the scheme given above can be simplified by assuming a given
hierarchy talks to the same model In J2EE, this approach is also known as
Composite View.[11] [PIC of an example of a hierarchy with real widgets]




Reimplement widgets to define methods for events. Annoying, proliferates classes.

Once notified, the views are in charge of fetching the new state from the
model: the view must therefore be aware of the model interface and its
semantics. 



Concerning callability on sone side or the other (e.g. event vs. method call)

forwarding is done depends on the degree of coupling you allow between the View
and the Presenter. If the view must invoke directly a Presenter's method,
obviously it must know its interface, so it must hold a reference to it and
know its interface. The alternative is that the view is oblivious to who is
listening, and just broadcasts events (commands) to report the button press.
The presenter observes these events and take appropriate action when triggered.
As you can see, the difference is subtle, and apparently irrelevant, but it can
be useful depending on the degree of coupling and self-containment of the view
vs. the controller (Presenter)




The presenter can be instantiated either by the client code, or directly by the
view. If this is the case, the View must know the model, so that it can
instantiate the Presenter and pass both the model and itself to it.

write something about preventing garbage collection when pubsub is used.

write that the view has two ways to interact with the controller and forward
events: strong coupling through direct invocation, or loose coupling through raising
events at a higher semantic level.

Add about a pattern where the View has a possibility to extract a "fill me up object" which is
then passed to the model. The model fills it with the new data and those automatically
change proper things in the view.

Detail the challenges of asynchronous component in testing


Design aims at managing complexity. The MVC details given in this book are guidelines, but
need to consider the actual real problem at hand. Some flexibility is needed. Strict
compliance generally produces a benefit, and has better communicative consistency within the
development team, but may not scale up to specific cases. In that
case, reconsider the design, or relax some constraints, but aim at keeping logic encapsulated
and object interaction simple and straightforward.



To prevent trashing with many notifications, there are three strategies:
- disable notifications, to the operations, re-enable the notifications.
  this has the disadavantage that you might not know what notifications to 
  send when they are re-enabled. One solution could be to spool them,
  and at re-enable, merge the duplicates and send out the minimum.
- have coarse grained operations, operating on large sets and sending out 
  only one notification at the end.
- Have fine grained modification routines with an option notify that allows
  to decide when to send the notification and when not to.
- Have the model be a centralizer of the notification delivery, but have notifyObserver called
  externally. 
- have a smart signal that can be put in a "trasaction on" mode, and accumulates the
  notifications, and then release the notification when a "commit" is issued

Problem with double notification if one notification is a subset of another.
e.g. contentChanged/lineMetaChanged and contentChanged/lineAdded. How to handle
the double notification? Pass an "event id" in the signal so that the client 
realizes that it's the same change that delivers two messages?

-

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

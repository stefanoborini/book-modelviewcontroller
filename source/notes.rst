Notes
=====
Local models, or one global model?

the view should be able to query or inform the controller for action (will, should, did): delegate


Compare OSX bindings with MVVM ? Same stuff?
You might have to fight your toolkit because it prefers a specific implementation of MVC
FIXME: relationship with apple, where the view is replaced with the child controller ?


All intralayer communication can only be routed through controller-controller connection. This connection is bidirectional.



following the hierarchic composition of the GUI nesting. The model can be the
same. In pratice, the scheme given above can be simplified by assuming a given
hierarchy talks to the same model In J2EE, this approach is also known as
Composite View.[11] [PIC of an example of a hierarchy with real widgets]



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


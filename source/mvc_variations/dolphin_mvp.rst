Dolphin Model-View-Presenter
----------------------------

The Model-View-Presenter (MVP) schema is a relatively small variation of MVC
which is concerned to the responsibility of handling user input and preparing
the data for the view. In MVC, the user action is directly handled by the
controller.  When a user clicks on a button, the click is attached to a
callback residing on a controller class.  In MVP, when the user interacts, the
click is handled by the view, which then forwards it to the Controller (now
called Presenter). This modification is known as "Twisting the triad".  How the
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

problem: Model and view are coupled, albeit loosely


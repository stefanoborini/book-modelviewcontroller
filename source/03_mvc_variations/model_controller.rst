ModelController
---------------

**Addressed Need:**

Objective-C style (MVA) design, or alternatively, the controller business logic
is merged into the model, and at that point it becomes a simple view/model
interaction. These designs are not necessarily wrong, but they tend to become
brittle or defining excessive responsibility, or making it hard to change the
model, the view, or the controller part if such need occurs.  In the
ModelController-View approach, the ModelController class is a Model with "GUI
intelligence": it knows how to manipulate its internal data in response to GUI
events, applying both consistency and business logic, while at the same time
being able to satisfy requests from View. The obvious disadvantage of this
approach is lack of flexibility and reuse of the Model, which becomes harder to
access and test. Additionally, while the Model can be a simple, "plain old"
object, the ModelController can depend on the GUI framework, since it must
interact with the View and UI events, preventing its reuse outside of the GUI
application. It is also difficult to handle multiple Views, because the
Controller part would have to handle GUI events coming from multiple Views.


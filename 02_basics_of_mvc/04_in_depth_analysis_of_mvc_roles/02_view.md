---
grand_parent: Basics of MVC
parent: In depth analysis of MVC roles
nav_order: 2
---
# The View

We introduced the View as the component of our application whose role is to
interact with the User, by accepting its input and showing the contents of 
the Model, and operates on it in **read-only**. Begin the face of the
application, is also the one that is more likely to change and adapt, often
under pressure of non-programming factors such as visual design and usability
needs.

A View listens for Model notifications and responds by fetching and rendering
the new state from the Model. This results in a strong dependency toward the
Model: Views must access Model data, something that requires full dependency
toward the Model's interface and existence.

Views are responsible for "purely GUI" intelligence, like handling behavior on
resizing, repainting, data displaying and visual formatting. They are also in
charge of handling primary events such as mouse clicks and keyboard key
presses, but should not perform any modifying action on the Model as a
consequence to these events. Instead, they should delegate this task to
Controllers. They should also not perform any operation that is competence of
the Model, nor store Model data, except for caching to improve rendering
performance. Cached data are never authoritative, and should never be pushed
back into the Model, or handed out to other objects. 

A View is generally composed out of **Widgets**, reusable visual building
blocks provided by a Widget toolkit library. Examples of widgets are buttons,
checkboxes, and menus. Complex interfaces are assembled from a collection of
Widgets, hierarchically contained in dialogs, windows and other visual
containers. This intrinsic hierarchic nesting must be factored in when we want
to go from the basic MVC given in the previous section to a real-world MVC. The
hierarchy is bidirectional, meaning that containers hold references to the
contained widgets, and vice versa. Widget state is normally modified from
client code via method calls, having no intelligence for receiving
notifications from the Model. A View adds Model observing capabilities and
rendering logic to a widget or groups of widgets, either through inheritance or
composition.

A view responds to Model notifications and repaint itself. This is, however, not
the only reason why a View may have to inquire the Model for data and repaint itself.
The view may have to do so after a show event.

MVC is not only limited to GUI representations, and Views are not necessarily
graphical objects. In fact, anything that can report information to the User in
some form can be classified as a View. For example, a musical notation Model
can be observed by two Views: one that shows the musical notation on screen and
another that plays it on the speakers. 

View can work also without a model, but of course it cannot display anything.
It can accept another model. In that case, it will unregister from the previous
one and register on the new one.

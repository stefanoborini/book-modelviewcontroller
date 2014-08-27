Taligent Model-View-Presenter (MVP)
-----------------------------------

**Addressed Need: Formalize the strategies given above for modern applications.**

Until now, we saw several strategies to address modern requirements such as
undo/redo, selection, and View-related state. Taligent, a subsidiary company of
IBM, formalized these strategies into the so-called Taligent
Model-View-Presenter architecture. An equally named, but different strategy is
the Dolphin Model-View-Presenter, which will be introduced later.  At first,
MVP seems complex, but in reality is a little step from what already introduced
in the previous sections. 
[PIC]
The aim is to divide responsibilities in simple, testable entities while moving
all logic away from the part that is most difficult to test, which is the View.
MVP is composed of the following parts:

   - A Model, whose role is purely business
   - a container level View.
   - Interactors, which is similar in concept to an MVC controlller. They handle user event and convert them into operations on the Model, through Command objects.
   - A set of Commands encapsulating operations that can be performed on the Model, supporting undo/redo semantics.
   - Selection: holds information about the subset of the Model that will be affected by the Command action.
   - Presenter, which is an overarching director object orchestrating allocation, initialization and interaction of the above objects. Generally, there's a Presenter for every View.


---
parent: Variations on the triad
---
# Taligent/IBM Model-View-Presenter (MVP)


Until now, we saw several strategies to address modern requirements such as
undo/redo, selection, and View-related state. Taligent, a subsidiary company of
IBM, formalized these strategies into the so-called Taligent
Model-View-Presenter architecture. An equally named, but different strategy is
the Dolphin Model-View-Presenter, which will be introduced later.  At first,
MVP seems complex, but in reality is a little step from what already introduced
in the previous sections. 

<p align="center">
    <img src="images/taligent_mvp/taligent_mvp.png" />
</p>

The aim is to divide responsibilities in simple, testable entities while moving
all logic away from the part that is most difficult to test, which is the View.

Taligent MVP organizes entities so that they can be divided into three classes:
A data oriented class, a GUI oriented class, and the Presenter.
The Data oriented class is composed of the following parts:

- A **Model**, whose role is purely of business.
- A **Selection**, holding information about the subset of the Model that will be affected by user's actions
- A set of **Commands**, encapsulating operations that can be performed on
  the Model according to the Selection, and supporting undo/redo semantics.

The GUI oriented class is instead composed of

- a View, representing the content of the Model, and accessing the Model directly.
- Interactors, mapping UI events at either low (mouse click, keyboard
  press) or high level (menu entry choice, click and drag selection) into actual
  commands to execute on the model. 

Finally, the Presenter class only contains the Presenter, which is an
overarching director object orchestrating the interaction of the above objects.
Generally, there's a Presenter for every View.

Having this structure has the advantage of distinguishing the range of application
of a given operation vs. the operation itself, through the Selection/Command distinction.
This simplifies the code, and solves notification issues so that notification is
sent only when the full operation is performed on all members of the selection.

Note that the MVP selection is not a Selection Model. It describes the selected
items in the Model on which a command is applied, but the visual representation
of this selection is in charge of the View. The Presenter is in charge of obtaining
that representation from the View, convert it into a MVP selection, and operate 
the commands with it. This results in the impossibility to share the visual
Selection among Presenters.


FIXME excessive confusion and overload of the terms "class", "object", "entity" 

Presenter as a coordinator of the process. One presenter per each view.

FIXME: widgets including both view and controller role. Presenter performs 
the active role in the model modification.
presenter is basically an application model.

chopped up the old MVC roles and reassigned. It seems like MVC, but its objects
aggregate different responsibilities.

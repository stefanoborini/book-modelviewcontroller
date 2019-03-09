---
parent: Variations on the triad
---
# Reenskaug MVC

### Motivation

Trygve Reenskaug formulated MVC first in 1979. His original approach is
different from modern forms of MVC, and for all purposes obsolete. It is
presented here to explain the historical formulation of MVC and its
motivations.


### Design

The best way to present Reenskaug MVC is to compare it against a 
Traditional MVC design. Like in Traditional MVC, Reenskaug MVC has:

- A Model representing knowledge about our data. 
- The View visually represents the Model, obtaining information by invoking 
  its methods. 
- The Controller has UI event handling duties, but for different reasons.

Crucial differences exist in the Controller, the View, and in a specialized 
object absent from Traditional MVC, the Editor:

- Reenskaug Controller handles UI visual layouting and UI primary events,
  converting these events into operations on the View. In Traditional MVC, 
  this is done by the View.
- Reenskaug View directly modifies the Model through Model methods calls.
  It does so with the assistance of an Editor. In Traditional MVC, this 
  is done by the Controller.

This design is a consequence of the technical environment of the time: Views' widgets
were simple renderings on the screen, with no functionality to receive and
process events from input devices. This task was assigned to Controllers.
At any given time, only one Controller was considered active
and would receive UI events from the event loop. Controllers were
organized in a hierarchy and had to negotiate the active status among
themselves in response to UI events and the expectations of the User/UI 
interaction. If a Controller found itself not authoritative to handle
a specific event, it would delegate to the Controller above in the hierarchy.

With the Controller performing layout/event handling duties, the
responsibility for Model modification was handled through an additional
player, the Editor, with cross-functional demands and dependencies.

An Editor is brought into existence on demand: the Controller asks the 
View for an Editor, which is presented to the User. UI events from the 
Controller are routed to the Editor, which converts these events in 
method invocations onto the View's API. Finally, the View modifies 
the Model.

### Reenskaug Controller 

With the introduction of smarter Views able to handle events,

 The third difference is the presence of the Editor as a
“View-extension helper” that the Controller uses in order to perform its task.
The reason for this design is that the Controller must have a View-contextual
entity to present to the User. For example, a GUI Label might require a
TextEdit field as an Editor, if the text is “free form”, but a ComboBox if the
label can only contain discrete values. Only the View part can know its
appropriate Editor.



into operations on the View. The View is not supposed to know about primary
events. 

Since then, widgets gained ability to handle events
In other words, most of the task initially assigned to a Reenskaug's
Controller are now taken care of by an underlying GUI framework. 


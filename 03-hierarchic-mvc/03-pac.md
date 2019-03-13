---
parent: 3 Hierarchic MVC
nav_order: 3
---
# 3.3 Presentation Abstraction Control (PAC)

PAC is an older scheme, very similar to HMVC. Similar to MVC, PAC defines a
triad (Agent in PAC terminology) as follows: Presentation, responsible for
handling all interaction with the user, both input (mouse events)  and output
(visualization) Abstraction, represents only data that are contextually
meaningful within the triad.  Control, connects Presentation and Abstraction,
plus acts as a communication hub in a Control-connected hierarchy of Agents.
Controls are responsible for forwarding the messages in transit in the
hierarchy, eventually after transforming them. When an agent wants to send an
event to another agent, it forwards it to its parent agent. The parent agent
either handles the event or, if it does not know what to do with it, sends the
event to one of its other children or to its parent,, and so on.  At first
glance, there's little or no difference between HMVC and PAC. If you think so,
you are not the only one [4]. There are however certain important differences.
First of all, HMVC  is based on traditional MVC, meaning that there's tight
coupling between the model and the view, with the view having to inquire the
model. In PAC, this communication is fully mediated by the controller. With
this strategy, PAC keeps MV loose coupling, while HMVC has MV tight coupling.  
The second major difference is the scope of access of the triads. In HMVC, each
triad is technically allowed to access all of the model. Not so in PAC. In PAC,
it can only access data that is contextually meaningful to that triad. If it
needs to access something that is not at its scope, it must forward an event to
the controller, which will be routed to the proper context by the hierarchy.

PAC: groups of PAC entities, each one composed by a Presentation, Abstraction and Control object.
organized in a network
- abstraction: represent the business functionality and state.

Control is a mediating controller. No interaction between P and A.



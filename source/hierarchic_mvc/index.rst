3. Hierarchic MVC
=================

Until now, we have seen MVC applied to a single triad. This works well for
individual widgets and dialogs, but how do we apply and scale MVC to an
application level?  Communication between controllers

Application composed of tens, or hundreds of triads. Can we organize them 
somehow? Do we need to? Yes we do.

Controller hierarchy in Traditional MVC
---------------------------------------

In order to handle the user events, traditional MVC had to organize controllers
in a hierarchy. When a View received an event, it was handed out to its controller
. Events are delivered according to the actual cursor presence (which basically
indicates which View is in Focus) until they rare given to a controller that is
willing to handle the event.



Hierarchic Model View Controller (HMVC, Recursive MVC)
------------------------------------------------------

Hierarchic MVC is a strategy to apply MVC in large applications while keeping
control of the granularity of data and communication. HMVC deploys a hierarchy
of triads by connecting controllers. The triads work together by handling
events they can handle, and forwarding them up in the hierarchy when they don't
know how to handle

[IMAGE]

There are relevant differences when compared with traditional MVC:
the view is responsible for handling user input events. These events are
forwarded to the controller.  The controller as usual performs modification on
the model through direct method call on model objects To refresh the view
state, the controller notifies the view that it needs refresh. The view then
communicates directly with the model, pulling the data from it without
involving the controller further. [4] Alternatively, the model notifies the
view by providing its own state [5] The controller also acts as a hub in the
controller hierarchy. If a controller receives an event from its associated
view that cannot be handled, it is bubbled to the parent, which in turn can
choose to handle it or delegate it further up or down in the tree.  Any model
at any level in the hierarchy can access data at any scope, and models can also
talk to each other. Controllers at any level in the hierarchy can share these
models.

controller has another controller as view
controller handle multiple views or multiple sub controllers


Presentation Abstraction Control (PAC)
--------------------------------------

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


Reenskaug MVC
-------------

Trygve Reenskaug formulated MVC first in 1979. His original approach is
different from modern forms of MVC. According to Reenskaug [1] [2], MVC has the
following characteristics: The Model represents knowledge about our data. No
difference here from traditional MVC The View visually represents the Model,
selecting what is relevant and what is not from the Model. The View knows the
Model and gets the information from the Model by invoking its methods. It is
also responsible for modifying the Model, again by invoking Model methods. The
View therefore “speaks the language” of the Model.  The Controller has both
layouting and event handling duties: it links the User to the system by
arranging and presenting the View on the screen and translating low-level user
events (e.g. mouse clicks) into high-level operations onto the View.  The
Editor is an extension to a Controller brought into existence on demand, and
used to modify data in response to User action. The controller asks the View
for an Editor, which is returned and presented to the User. The Editor accepts
the User events, and deliver them (after translation) to the View to applying
the changes to the Model.  As you can note, there are a few important
differences from traditional MVC. The first is in the roles of the Controller
and the View: in Reenskaug MVC, the View is in charge of modifying the Model
under instruction of the Controller and Editor, while in traditional MVC the
View knows the Model but only in “read only”: all operations that modify the
Model are issued by the Controller.  One advantage of Reenskaug's MVC is that
User action can be emulated by replacing the standard Controller with a mock
Controller performing stress-test operations, something extremely useful for
testing. 
A second difference is in the Controller: Reenskaug's Controller performs
operations such as layouting the Views on the screen, converting primary events
into operations on the View. The View is not supposed to know about primary
events. In other words, most of the task initially assigned to a Reenskaug's
Controller are now taken care of by an underlying GUI framework. This
difference is a child of its time: widgets were just a form of pure visual
rendering, with no functionality to receive and process events from input
devices.  The third difference is the presence of the Editor as a
“View-extension helper” that the Controller uses in order to perform its task.
The reason for this design is that the Controller must have a View-contextual
entity to present to the User. For example, a GUI Label might require a
TextEdit field as an Editor, if the text is “free form”, but a ComboBox if the
label can only contain discrete values. Only the View part can know its
appropriate Editor.

Only one model per view.

View initializes its controller

only one controller is active at a time, because only one controller is technically
able to receive the input from the user. It is assumed that there is a coordination
of the controllers, typically in a hierarchy, so that if the current one is not authoritative
to handle a specific event, it delegates it to the upper controller.

Similar to a unix architecture, with stdin (controller) and stdout (view)

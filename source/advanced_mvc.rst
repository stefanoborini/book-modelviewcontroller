Advanced MVC
============

Model persistence
-----------------

In some cases, the model or part of the model must be made persistent (for
example, to disk) to be restored at a later stage. Which component should be
responsible for the persistence?  The most natural strategy is to let the model
know how to store and retrieve itself from disk or database. This is a popular
solution and goes by the name of "ActiveRecord". It is simple to use and
understand, relatively flexible and intuitive, but it's not without limitation.
The first, and biggest limitation is that it favors strong coupling between the
model and the IO strategy: abandoning the local disk storage in favor of a
remote database will force us to reimplement the IO strategy of all the model
objects; A second problem is that Model objects lifetime is related to the
storage backend. This makes testing the Model much harder, because the storage
backend must be fully functional, or mocked; Finally, if the Model is fully in
control of its persistence strategy, the client code cannot decide differently,
for example, if it wants to  store the model object somewhere else.
An alternative strategy is to delegate persistence to the controller. The
controller holds a reference to the model, and to a Storage subsystem. In
response to proper trigger events, the controller can pick the relevant model
objects and push them to the storage subsystem. This strategy has a few
advantages: the model objects are lighter and know nothing of storage
strategies, which can now be changed freely by using a different Storage
service, potentially to a mock object during testing. The main disadvantage is
that the additional flexibility requires more a complicated interaction.  The
storage can also be in charge of additional tasks, such as search and filtering
of model objects, or creation (factory) of new objects, which the storage
inserts into the database and hands out to the controller.
When it comes to data formats, there are many options, from the very simple CSV
to the more complex like databases. A simple choice can be a nosql database, or
a tinysql. Regardless of your choice, it's important you version your objects.
ORM models

Vetoing the changes
-------------------

Model distribution
-------------------
The model can be distributed over a network and accessed through proxy classes
with none or minor changes to the remaining protagonists. 

Sharding

Scriptability
Modification of the model programmatically can enable scripting
Testing


In general, you should be able to test or even use the model
independently of the controller and views. In fact, the model should
be able to work without any controllers or views implemented at all.
It's a completely separated layer with no dependencies toward GUI
representation, widgets, or strategies to apply the changes. If this
is not the case, then you have a code smell that needs refactoring.
There are however exceptions to this rule [7]. For example, suppose
your model is representing the state of a drawing program. The shapes
that are inserted in the model are actual Shape objects that are
graphical in nature, and it would make sense to assign to these
objects the responsibility of drawing themselves on the view. This is
practical, but it can backfire: it requires the objects to know about
the specific view's details about how to draw itself onto it, meaning
that a different view might not be compatible. Assigning
representation responsibilities to model objects is a rare occurrence
that can always be worked around, for example separating the
mathematical description of the Shape (e.g. the corners of a
rectangle) from the drawing logic (e.g. the actual graphic calls that
draw the rectangle on the screen) and move this drawing logic in a
Renderer class. 


A view that acts on a widget knowing nothing about the model. View
“adapter”






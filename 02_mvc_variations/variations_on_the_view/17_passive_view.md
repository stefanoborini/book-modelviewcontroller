Passive View
------------

A major problem resulting from a complex View is the difficulty of testing.
Visual components tend to be more complex to test, requiring events to be
dispatched correctly and asynchronously. Using an approach where all the logic
of the View is moved to non-GUI objects would greatly improve ease of
testability. The **Passive View** (also referred as **Humble Dialog** or
**Humble View**) approach has exactly this objective.

Passive View keeps the View humble in logic and with no awareness of the Model. 
The View is normally made of off-the-shelf widgets from a widget set. It
contains no application-related logic, thus removing the need for
specialization of the View or of the Widgets classes to introduce this logic. 

With this design, all business code goes in the Controller or the Model.
In particular, the Controller is now in charge of the synchronization 
of the View's contents, either through the View's set/get methods, or 
directly on the widgets. The Controller and all its logic can be tested
effectively against a mock View. The actual View, having no logic, can be 
left untested.

The mechanism of action is the following:

1. When the View receives user events, they are forwarded to the Controller
   as in Traditional MVC.
2. The Controller acts on the Model.
3. Either immediately, or in response to a Model notification, the
   Controller now updates the data displayed by the View's widgets,
   to synchronize them against the new Model contents.

The negative consequence of this approach is the greater burden of complexity
transferred on the Controller, which now has to deal with visual logic,
visual semantics, and due to the potentially void nature of the view, also 
data validation.

. If this logic becomes excessively complex, it can be
further extracted in a support Backend object acting in-between the View
and the Controller, and dealing exclusively with the View's presentation needs.

The big advantage of a Passive View is that it makes testing the controller 
easier. The View can be completely replaced with a mock object implementing the
same interface. When testing the Controller, the mock View's methods will 
be called, and their invocation can be checked by the test. The mock View can
also be set up to present specific data to the Controller.  Testing the actual
View is generally left out. Due to its passive nature, it's generally made of
off-the-shelf widgets that are assumed as well-behaved.



Once again, the View's Backend can easily be tested against a mock View.

The View's interface should accept only primitive types, so that no
complex data unpacking and manipulation is performed inside.


FIXME: Controller notifies the view that changes have occurred on the model
FIXME: connection with passive model.


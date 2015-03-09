Passive View
------------

A major problem resulting from a complex View is the difficulty of testing.
Visual components tend to be more complex to test, requiring events to be
dispatched correctly and asynchronously. Using an approach where all the logic
of the View is moved to non-GUI objects would greatly improve ease of
testability. The **Passive View** approach has exactly this objective.

Passive View (also referred as Humble Dialog or Humble View) keeps the
View humble in logic and with no awareness of the Model. 
The View is normally made of off-the-shelf widgets from a widget set.
It contains no application-related logic, thus removing the need for
specialization of the View or of the Widgets classes to introduce this logic. 

With this design, all business code goes in the Controller or the Model.
In particular, the Controller is now in charge of the synchronization 
of the View's contents, either through the View's set/get methods, or 
directly on the widgets. The Controller and all its logic can be tested
effectively against a mock View. The actual View, having no logic, can be 
left untested.

The mechanism of action is the following:

    #. When the View receives user events, they are forwarded to the Controller
       as in Traditional MVC.
    #. The Controller acts on the Model.
    #. Either immediately, or in response to a Model notification, the
       Controller now updates the data displayed by the View's widgets,
       to synchronize them against the new Model contents.


The negative consequence of this approach is the greater burden of complexity
transferred on the Controller, which now has to deal with visual logic and
visual semantics. If this logic becomes excessively complex, it can be
further extracted in a support Backend object acting in-between the View
and the Controller, and dealing exclusively with the View's presentation needs.
Once again, the View's Backend can easily be tested against a mock View.

The View's interface should accept only primitive types, so that no
complex data unpacking and manipulation is performed inside.


FIXME: Controller notifies the view that changes have occurred on the model
FIXME: connection with passive model.

Passive view can be mocked totally. The mock just needs to implement the same
interface. The controller will then call these methods and the result can be
checked on the mock.
Generally, a passive View does not need much testing per-se, because it's
built out of well established widgets. 

due to the potentially void nature of the view, Validation is best assigned to
the controller.


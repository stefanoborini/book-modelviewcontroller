Passive View
------------

A **Passive View** strategy keeps the View completely under direction of the
Controller, both for the handling of events and for the updating of its
contents.  The mechanism of action is the following:

    #. When the View receives user events, they are forwarded to the Controller
       as in Traditional MVC.
    #. The Controller acts on the Model.
    #. Either immediately, or in response to a Model notification, the
       Controller now replaces the data displayed by the View's widgets,
       to synchronize them against the new Model contents.


[PICTURE]

With a Passive View, all business code goes in the Controller or the Model.
The View is normally made out of off-the-shelf widgets from a widget set. It
contain no application-related logic, thus removing the need for specialization
of the View or Widgets classes to introduce this logic. Additionally, the
Controller can be tested effectively against a mock View, while the View
can be safely left untested.

The negative consequence of this approach is the greater burden of complexity
transferred on the Controller, which now has to deal with visual logic and
semantics.


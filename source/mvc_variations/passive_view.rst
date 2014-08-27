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



.. todo::

    completely unrelated. It must go somewhere else.

    When the view is shown, it will have to update its content. However, if the
    view is not visible, it should not receive events, so it should either
    unsubscribe from the model when hidden, or mute the delivery by first checking
    if it's visible before proceeding to update itself. The reason is that if a
    view is connected to the model, and this view requires time to refresh itself,
    we don't want to trigger this refresh if the view is not visible to the user.



Passive View
------------

Passive View is a variation of MVC where the view is completely under direction
of the Controller, both for the handling of events and for the updating of the
View contents. The advantage is that all application code goes in the
controller, which can be tested effectively. The view is therefore normally
made of standard components from a widget set, with no application-related
intelligence.

When the view is shown, it will have to update its content. However, if the
view is not visible, it should not receive events, so it should either
unsubscribe from the model when hidden, or mute the delivery by first checking
if it's visible before proceeding to update itself. The reason is that if a
view is connected to the model, and this view requires time to refresh itself,
we don't want to trigger this refresh if the view is not visible to the user.



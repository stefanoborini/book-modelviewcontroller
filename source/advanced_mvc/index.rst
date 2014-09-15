Advanced MVC
============


Vetoing the changes
-------------------

Some interface design may require vetoing of a specific change on the Model.
Vetoers are specific listeners to the model. When the model is requested to change
a value, it issues an aboutToChange() notification, passing the new intended
value. This event is reported to the listeners which evaluate the proposed
change and respond with an ok/not ok state. As the model notifies all vetoers,
it collects the responses and aborts the change if one vetoer returns the
change as not ok. If all vetoers approve the change, then the change is
performed and the model issues a changed().

Model distribution
-------------------

Scriptability
Modification of the model programmatically can enable scripting

.. toctree::
   :maxdepth: 2

   model_persistence
   mvc_testing


Event bus



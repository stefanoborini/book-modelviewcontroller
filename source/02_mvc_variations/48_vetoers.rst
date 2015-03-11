Vetoing the changes
-------------------

Some interface design may require vetoing of a specific change on the Model.
Vetoers are specific listeners to the model. When the model is requested to change
a value, it issues an aboutToChange() notification, passing the new intended
value. This event is reported to the listeners which evaluate the proposed
change and respond with an ok/not ok state. As the model notifies all vetoers,
it collects the responses and aborts the change if one vetoer returns the
change as not ok. If all vetoers approve the change, then the change is
performed and the model issues a changed(). An example of this mechanism
is the "constrained property" in javabeans.

Change vetoing can be useful to extract complex validation logic from
the model into pluggable or reconfigurable objects. 

Typically validation happens at the View level (e.g. widgets don't allow 
introduction of specific values, or there's a vetoer for the widget: Qt Validators)
or at the model level (raises an exception if some invalid data is passed)
Vetoers give more flexibility than the second option, while enforcing
business constraints at the model level. 



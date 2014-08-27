Passive Model
-------------

**Addressed Need: Use a Model without notification features.**

Traditional MVC uses the so-called **Active Model**: when the Model changes in
response to an action, it notifies its listeners of the occurred change. This
approach is excellent to deal with multiple listeners, multiple Controllers,
and the need to notify about Model changes coming from external sources.

The Active Model strategy has a counterpart in the **Passive Model**. A Passive
Model does not perform notification. Instead, this task is orchestrated by the
Controller:

   #. The Controller modifies the Model.
   #. The Controller informs the View to update itself.
   #. The View now inquires the Model contents as in the Active case.

The activity diagram details the steps given above

.. image:: ../_static/images/PassiveModel/passive_model.png
   :align: center

A mild advantage of this approach is that any object can be used as a Model,
even when it does not provide notification functionality. In practice, a
Passive Model can always be converted into an Active one either through
inheritance or by using a wrapper class satisfying the Passive Model's original
interface. This wrapper will receive change requests from Controllers, delegate
the change requests to the Passive Model, and finally notify the listeners.
This solution is particularly useful for an already developed business object
that knows nothing about MVC and must be made part of a triad.

The major shortcoming of a Passive Model is that it doesn't work if the Model
can change through multiple sources (for example, other Controllers connected
to the same Model, or if the Model is a frontend to a database and another
client modifies the data), nor it can handle updating of multiple listeners. 

Despite its apparent lack of potential, a Passive implementation has its area
of excellence in Web-based MVC, where the fundamental nature of the HTTP
protocol prevents the Model to perform notifications to the View. We will
examine this mechanism in more detail in Chapter FIXME.


.. todo::
   On the web, the View is delivered to the client side for rendering in the
   browser, and the
   Model stays on the server side. When the User performs an action, the
   Controller will issue a change request to the Model, followed by a request to
   the View to refresh itself. The View will now issue a get request to the server
   to synchronize with the new Model contents.






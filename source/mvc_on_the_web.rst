MVC On the web
==============

On the web, the controller is responsible for handling user events, preparing
the view, and pushing it to the renderer. a quite different pattern.

MVC can also be used on the web, and plenty of web development frameworks
provide for free a well designed MVC architecture, where the programmer has
just to fill the empty spaces and all the web heavy lifting is taken care of.
As usual, the model objects represent the business domain of our application,
with the task of persistence given to the model or to another layer: they
either talk to a database directly (generally, but not always, an SQL one) or
through an Object-Relational Mapper to convert the Object Oriented nature of
the model classes into something a relational database can digest.  Similarly,
the Controller receives the HTTP request from the user, as dispatched by the
Web framework. It is responsible for applying business logic and coordinating
the other objects to display the final web page (or parts of it) to the user.
In general, what the controller does at this point is to parse the request,
selects the proper model objects to honor this request, selects a view
appropriate for the request and let the view the task of rendering the final
HTML for the browser's consumption. To do so, the view normally combines the
controller-provided data with a template mechanism.

On the web, the separation between the View (the HTML and the browser as a
renderer) and the Controller (the server side of the code) is strong and with a
bottleneck in communication.

The controller can switch model or views as it sees fit, but in general it is
initialized and deeply related to the view. How the controller get to know
these different models or views can be done either through accessor methods
(external code "pushes" the new model to the controller) or through a provider
class (e.g. the controller knows where to get a model: the provider class hands
it out when needed).  knockout.js

Something about REST in web mvc
Front controller
Page Controller


To keep the view and the controller synchronized, there are two possible approaches:
“push” strategy: data is pushed by the controller into the view.
“pull” strategy: data is pulled by the view from the controller

For example, suppose the user adds a comment to a forum. Once he submits the
request, its comment is now accepted by a controller, which will add it to the
model. The view and the model are now desynchronized. The controller now can
reply by pushing the new information to the view, so that the user-submitted
comment can appear. Any other comment that was added to the model will also be
pushed into the view, allowing the user to see its view change as comments are
added.

In the pull model, the view is responsible for requesting and fetching data
from the controller at the end of the submit request, and synchronize its
content. Pull is also generally used to fetch any kind of data from the
controller in response to a user request.

spring

ruby on rails

wxpy

On the web, the View is delivered to the client side for rendering in the
browser, and the
Model stays on the server side. When the User performs an action, the
Controller will issue a change request to the Model, followed by a request to
the View to refresh itself. The View will now issue a get request to the server
to synchronize with the new Model contents.






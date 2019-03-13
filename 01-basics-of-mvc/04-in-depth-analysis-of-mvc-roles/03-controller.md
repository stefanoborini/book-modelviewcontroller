---
grand_parent: 1 Basics of MVC
parent: 1.4 In depth analysis of MVC roles
nav_order: 3
---
# 1.4.3 The Controller

The last of the components of MVC, the Controller, has the heavy duty task to
make things happen by gathering, validating, and processing User events to
modify the state of the application. It operates on the Model in **read-write**.

Controllers are associated to Views in a strong one-to-one mutual dependency,
and can be described as the “business logic” of the View. When the View
receives a primary event, it forwards execution to an appropriate Controller
method, where appropriate logic modifies the state of the application.
Generally, the change is applied to the Model, but depending on the problem the
Controller can also directly modify the View, in particular when it changes
visual state that is purely pertinent to the View and is not represented in the
Model. Examples of these cases can be enabling/disabling some widget,
scaling/zooming of a plot area, reordering of menu entries and so on. 

A Controller generally hosts a reference to its View and the Models it
modifies, and depends strongly on their interfaces and presentation semantics,
at least to a degree. It may act on Models that are not the ones observed by
the associated View. Like Views, a Controller can be a listener for Model
notifications, when the Model state influences how the Controller interprets
the User events. 


the controller can act on the model, or directly on the view, if it needs to change
the visual representation without involving a change in data.

specify that it's _not_ View == read-only widget vs Controller == read-write widget.

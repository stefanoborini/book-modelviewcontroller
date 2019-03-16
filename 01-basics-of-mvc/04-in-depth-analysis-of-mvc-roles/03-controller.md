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
method, where the appropriate logic modifies the state of the application 
held by the Model.

A Controller generally holds a reference to its View and the Models it
modifies, and depends strongly on their interfaces and presentation semantics,
at least to a degree. It may act on Models that are not the ones observed by
the associated View. Like Views, a Controller can be a listener for Model
notifications, when the Model state influences how the Controller interprets
the User events. 


the controller can act on the model, or directly on the view, if it needs to change
the visual representation without involving a change in data.

specify that it's _not_ View == read-only widget vs Controller == read-write widget.

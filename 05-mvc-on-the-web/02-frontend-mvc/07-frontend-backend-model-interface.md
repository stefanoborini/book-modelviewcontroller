---
grand_parent: 5 MVC on the web
parent: 5.2 Frontend MVC
nav_order: 7
---
# 5.7 Frontend/Backend interfaces

Web models tend to have two responsibilities:

- frontend role, to communicate with the User.
- backend role, to communicate with administrative tools.

It is useful to keep the model lean and constrained to have the following design

- ModelBase: containing the basic functionality for data access.
- ModelFrontend: Reimplements ModelBase, implementing Frontend API.
- ModelBackend: Reimplements ModelBase, implementing Backend API.


Backbone is a JavaScript library providing MVC for Web development.
Models support active notifications for individual attributes.
Persistency is supported via a REST API for both individual
Model objects and for collections. Through the REST API, 
objects on the client side are persisted on the server via CRUD
operations. Alternative persistence backends are possible.
It supports Signals (backbone.Events)

THere is no controller in backbone. 

backbone supports data binding through backbone.stickit.
Views describe which elements in the DOM match with which
entries in the Model. Data can be manipulated (onSet/onGet) while
in transit.

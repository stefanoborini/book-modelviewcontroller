---
parent: MVC Implementations
---
# Backbone JS

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

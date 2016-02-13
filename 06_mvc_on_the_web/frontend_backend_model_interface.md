# Frontend/Backend interfaces

Web models tend to have two responsibilities:

- frontend role, to communicate with the User.
- backend role, to communicate with administrative tools.

It is useful to keep the model lean and constrained to have the following design

- ModelBase: containing the basic functionality for data access.
- ModelFrontend: Reimplements ModelBase, implementing Frontend API.
- ModelBackend: Reimplements ModelBase, implementing Backend API.




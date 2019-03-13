---
parent: 5 MVC on the web
nav_order: 1
---
# 5.1 Front controller

The front controller (sometimes called Application) is the first point of entry
for the request. It handles the overall dispatch to the relevant controller,
and deals with common needs such as authentication, session management,
security, redirection. It contains logic that all requests must consider,
reducing code duplication. It also adds data to the execution context.

Dispatch to the front controller is performed directly from the webserver.

Typically, the front controller can host a list of intercepting filters, classes aimed at
performing specific operations on the incoming request.

A front controller can be a potential bottleneck. All requests pass through it.

FIXME: different interpretation of front controller. a single point of entry that replace
the page controller design. The front controller creates commands (which replace page controllers)
according to the submitted request, and these commands are executed by the front controller.
Commands feed information to the views.

FIXME: django approach is kind of mixed. There's a front controller that dispatches to methods
that in practice become page controllers. Before the dispatch happens, the request is passed
through filters (middleware)



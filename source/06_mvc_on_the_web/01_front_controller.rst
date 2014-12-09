Front controller
----------------

The front controller is the first point of entry for the request. It handles the overall
dispatch to the relevant controller, and deals with common needs such as authentication,
session management, security, redirection. It contains logic that all requests
must consider, reducing code duplication. It also adds data to the execution context.

Dispatch to the front controller is performed directly from the webserver.

Typically, the front controller can host a list of intercepting filters, classes aimed at
performing specific operations on the incoming request.

A front controller can be a potential bottleneck. All requests pass through it.



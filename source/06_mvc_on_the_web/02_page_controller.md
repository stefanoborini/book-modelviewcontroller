Page controller
---------------

A page controller handles a specific request on the server, by combining model and view and send back to the client the rendered view. Normally, it is bound to a specific URL.

It normally handles one logical page, or one specific action. This makes it extremely simple.

Once it receives the request, it extracts data from this request (e.g. HTTP
headers, query parameters, cookies, form contents), performs operations on the
model, then select the proper view to perform rendering. A template mechanism
is generally used to render model data while separating rendering/presentation
logic. It can render a whole page, a subset of it, or data that are parsed by
the client-side javascript.

Testing the page controller can be complex due to the need to simulate an HTTP
request. Ideally, one would partition non-HTTP related functionality and make
them testable without an HTTP context, otherwise the web framework environment 
must be present and set up.

The page controller often is implemented as a reimplementation of a base class,
to provide reusable functionality that is common to all page controllers. 

In general, functionalities like session management, authentication, and similar
low-level operations are not handled at the page controller level. A different technique
is used: Filters (aka Middleware)


FIXME: common functionality between different page controllers may require inheritance.
This can force hierarchies that not necessarily are appropriate, and force refactorings
as new pages are added.


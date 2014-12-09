Page controller
---------------

A page controller handles a specific request, by combining model and view and send back to the client
the rendered view.

It normally handles one logical page, or one specific action. This makes it extremely simple.

Once it receives the request, it performs the operation on the model, then select the proper view
to perform rendering. A template mechanism is generally used to render model data while separating
rendering/presentation logic. It can render a whole page, a subset of it, or data that are parsed
by the client-side javascript.

Testing the page controller can be complex due to the need to simulate an HTTP request. Ideally, one would
partition non-HTTP related functionality and make them testable without an HTTP context, 

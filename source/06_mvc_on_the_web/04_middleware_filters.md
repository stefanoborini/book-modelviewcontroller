Middleware filters
------------------

There are operations that are common and require a lot of pre or post processing
in web handling. Things like authentication, session management, compression,
cookie extraction, logging, and so on.  It's common to provide the code dealing with
these issues as pluggable components called Intercepting Filters or Middleware.
These operations are common to all pages and it's convenient to centralize
them. They also tend to be agnostic of the actual application, therefore
offering a huge reuse potential.

Filters are generally not dependent on each other. When they are, it's important
that they are traversed in the proper order.

They act as pre-processing filters of the request and post-processing
filters of the response.

Considering that all requests traverse these filters, their performance is of
the highest importance.

[FIGURE: put a layered request -> f1 f2 f3 controller -> response -> f3 f2 f1]

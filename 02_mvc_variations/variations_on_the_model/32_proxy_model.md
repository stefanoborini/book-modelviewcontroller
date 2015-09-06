# Proxy Model

-----------
**Note**: In the context of Qt MVC, a Proxy Model is a Model Pipe design.

-----------

Replaces a model and acts according to the Proxy pattern.
Useful for Network communication, to load lazily information from
the database or disk.

a proxy model can also prevent data copying. For example, it can
map indexes (e.g. pipe filter)

You can obtain the data from a broad choice of technologies:
http request, sql query, rmi, rest.

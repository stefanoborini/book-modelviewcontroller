Proxy Model
-----------

Replaces a model and acts according to the Proxy pattern.
Useful for Network communication, to load lazily information from
the database or disk.

caching: instead of hitting the database, hold the information.
loading only information that is relevant, withholding bulkier
information, but providing a mechanism to access it once needed.
(FIXME maybe move to advanced techniques? where does it fit?)



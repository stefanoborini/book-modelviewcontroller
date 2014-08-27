Visual Proxy
------------

Holub argues the following [3]:
It is very rare for the same Model to be represented at the same time in two
different ways Model representation is not about the model object per-se, but
for some attributes.  these attributes are generally presented in the same way
regardless of where they will appear in the dialogs.  In OO design,
unrestricted access of internal state via get/set routines is a faux pas In
design, thus nullifying part of the approach the controller might use to modify
the Model.  Essential separation between model and view are impossible to
achieve in MVC, which does not scale well at the application level.  Model
objects should create their own UI for their own attributes, as this does not
violate encapsulation as a get/set model did, and because reuse of model
objects would not be compromised, both because reuse is rare if ever, and the
representation of an attribute is generally implicit in the attribute itself.


The controllers should be visual widgets that have read-write properties, not
“stay behind” classes that are delegated.  Data binding



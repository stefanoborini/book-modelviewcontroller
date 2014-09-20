MVC Pluggable View
==================

As part of the original MVC specification, a typical problem once encounters is that some
Views are very similar: they need to have some logic that extracts the data from a Model,
and present it in the same way. It aims at reducing the need for subclassing a generic View
object.

MVC Pluggable Views is very similar in concept to ValueModel. 
The difference is that, instead of having a generic View that calls a specific model
on an adaptor object, the adapting logic is passed to the View itself at construction
as a function. When the View needs to access the Model, it uses this logic to retrieve the value.

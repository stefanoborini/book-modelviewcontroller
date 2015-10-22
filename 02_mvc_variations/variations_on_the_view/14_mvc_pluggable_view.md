# Pluggable View

### Motivation

For some applications, different Views may have the same implementation for 
the UI part, but different implementation for data extraction from the Model.
To prevent duplication, a possible solution is to implement the common UI logic in a base View class, and have subclasses reimplementing the data extraction
logic.

A second solution is to use a Value Model, which puts the extraction logic
on a Model adapter object, transforming the Model's complex interface into 
a trivial getter/setter pair. The resulting View is agnostic of the nature 
of the Model and the complexity of the extraction logic.

Pluggable View provides a third strategy: the extraction logic is injected at
View's initialization by the client code. 

### Design

The View's constructor accepts a function object containing the data 
extraction logic. This function accepts the Model object and returns
the relevant data needed by the View.

The View listens to the Model for change notifications. When a change occurs,
the View calls the function object passing the Model, and obtains the relevant
information as a return value.

Variations of this solution allow for multiple functions to extract different parts of the Model, or the possibility to swap the function object after construction.

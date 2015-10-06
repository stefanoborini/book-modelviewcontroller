# View-aware Model

### Motivation

This unconventional design breaks a fundamental rule of MVC: 
rather than having the View getting data from the Model, the Model acts 
on the View to populate it.

This design comes with a hefty price of dependency of the Model 
towards the different Views' interfaces. This price can be mitigated 
by having a generic interface ``GenericViewInterface`` that abstracts 
individual View's differences. The Model knows about this generic 
interface and only invokes its methods. Implementations of this
interface are on their associated View and transform the Model's generic
setting invocation into a specific action on the View.

On Model change, the View will pass its own specific implementation of the GenericViewInterface
to the Model. The Model will now invoke the GenericViewInterface methods, passing its own content.
These methods will then act on the Views. 

For testing purposes, the GenericViewInterface can be implemented by a mock
class, and the individual state of the resulting Mock object can be inquired after being
passed to the Model.


The Model can even create the View. See Holub's.
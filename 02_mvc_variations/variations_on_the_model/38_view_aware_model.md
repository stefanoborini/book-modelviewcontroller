# View-aware Model

### Motivation

This unconventional design breaks a fundamental rule of MVC: 
rather than having the View get data from the Model, the Model 
acts on the View to populate it.

A View-aware Model seem to have conceptual closeness to Visual Proxy,
but they handle different concerns: 

- Visual Proxy deals with View's creation. The Model acts as a 
  factory for the View. 
- View-aware Model deals with data synchronization. The Model knows
  about the View and acts on it.

A View-aware Model instead can be seen as a combination of a 
ModelController and a Passive View.

### Design

The Model holds a reference to the View. When a Model change occurs, 
it directly calls the View's specific method to change its visual aspect.

<p align="center">
    <img src="images/view_aware_model/view_aware_model.png" />
</p>

This design comes with a hefty price of dependency of the Model 
towards the View's interface. The consequence is that driving multiple 
Views with different interfaces becomes cumbersome. 
This price can be mitigated by having a generic interface that 
abstracts individual View's differences: the Model knows this generic 
interface and invokes its methods. Different Views implement it and 
handle the call into appropriate action on their widgets. Although this
mechanism may seem to become a notification system, observe that 
in a View-aware Model approach the View does not retrieve the data
from the Model in response to the call.

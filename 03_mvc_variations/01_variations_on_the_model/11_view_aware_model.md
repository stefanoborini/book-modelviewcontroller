---
grand_parent: MVC Variations
parent: Variations on the Model
nav_order: 11
summary: A model that knows its views interface beyond simple notification delivery.
---
# View-aware Model

### Motivation

This unconventional pattern breaks a fundamental rule of MVC: 
rather than having the View get data from the Model, the Model 
acts on the View to populate it, by pushing its data through the View
interface.

A View-aware Model can be seen as a combination of two patterns:
ModelController and Passive View. It is a pattern of limited  
practical use, but can be useful to recognise.

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
handle the call into appropriate action on their widgets. 


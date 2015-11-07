# ModelController

### Motivation

In some implementations, Model state may be small and only relevant 
for a specific View, making the split between Model and Controller 
classes excessive. In these cases, Model and Controller 
can be merged to define a ModelController, which can be interpreted 
either as a "Model with GUI intelligence", or as a "Controller 
with State". The View dispatches UI events to the ModelController,
which alters its state and notifies the View of changes.

Compared to a traditional split solution, ModelController is 
less flexible, less reusable, harder to access and test. 
It carries a dependency against the UI, something that might 
prevent its reuse outside of a UI application. 

In addition, ModelController makes difficult to handle multiple Views.
The motivation is twofold: first, the Controller part would have to 
differentiate which View is sending a given event. Second, 
different Views may have a different visual implementation and thus 
generate different types of events. The ModelController interface 
would have to accommodate nomenclature and behavior of all Views, 
leading to a bloated and complex interface.

A ModelController approach is not necessarily wrong, but tends to become
brittle and is therefore limited to straightforward cases.

### Design

ModelController hosts the logic to manipulate its internal state 
in response to GUI events, applying both consistency and business logic,
while at the same time being able to satisfy requests from the View. 


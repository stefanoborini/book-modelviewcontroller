# ModelController

### Motivation

In some implementations, Model state may be small and only relevant 
for a specific View, making the split between Model and Controller 
classes excessive. Merging these classes leads to a ModelController, 
which can be seen as a "Model with GUI intelligence", or as a "Controller 
with State". 

Compared to a traditional MVC solution, ModelController has the following
disadvantages:
- it is less flexible, less reusable, and more complex to test.
- potentially carries a dependency against the UI layer if, 
  for example, needs to interpret pure UI events. This complicates
  its reuse outside of a UI application. 
- as stated in the opening paragraph, it complicates handling of 
  multiple Views

The motivation for the latter point is twofold: first, the Controller 
part would have to differentiate which View is sending a given event. Second,
different Views may have a different visual implementation and thus generate
different types of events. The ModelController interface would have to
accommodate nomenclature and behavior of all Views, leading to a bloated and
complex interface.

A ModelController approach is not necessarily wrong, but tends to become
brittle and is therefore limited to straightforward cases.

### Design

The View dispatches UI events to the ModelController,
which alters its state and notifies the View of changes.

ModelController hosts the logic to manipulate its internal state 
in response to GUI events, applying both consistency and business logic,
while at the same time being able to satisfy requests from the View. 


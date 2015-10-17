# ModelController

### Motivation

Sometimes it is not needed to extract a separate, non UI-aware Model. The
state may be small and only relevant for the specific View, making the 
split between the two excessive.

In these cases, Model and Controller can be merged to define a 
ModelController, which can be interpreted either as a "Model with GUI
intelligence", or as a "Controller with State"

ModelController hosts the logic to manipulate its internal state 
in response to GUI events, applying both consistency and business logic,
while at the same time being able to satisfy requests from the View. 

The obvious disadvantage of this approach is lack of flexibility and reuse 
of the Model, which becomes harder to access and test. UI events need to be
created and dispatched to the ModelController from the View. 

Additionally, while a Model can be a simple object with no dependencies
against the UI framework, the ModelController might have to have this 
dependency, since it must interact with the View and the GUI events.
This dependency might prevent its reuse outside of the GUI
application. 

Finally, a ModelController makes difficult to handle multiple Views.
The motivation is twofold: first, the Controller part would have to 
handle GUI events coming from multiple Views, introducing the need 
to differentiate them. Second, different Views may generate different
events from different widgets. The ModelController interface would have 
to deal with the nomenclature and behavior of each individual View and
accommodate each of them. The resulting ModelController interface would 
potentially become bloated and hard to understand.

A ModelController design is not necessarily wrong, but tends to become
brittle and is therefore limited to straightforward cases.
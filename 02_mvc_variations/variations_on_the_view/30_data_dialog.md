# Data Dialog

### Motivation

**Need: Fire and forget dialog to get information from the user**

Data Dialog is a simplified design to obtain information from the User.
It can normally be used for preferences dialogs. The optimal set of requirements
for the design simplify GUI interaction considerably, giving the Data Dialog 
approach its chance to shine:

 - The dialog must be Modal (i.e. its presence disallows interaction with other widgets in the same
   application)
 - The dialog allows only Accept ("Ok" button) and Reject ("Cancel" button) strategies.
 - It must not need synchronization tracing the application status.

The typical interaction strategy is as follows: the backend code gathers all
relevant information and puts this information in a plain data object, e.g. a
dictionary.  Next, a DataDialog object is instantiated, and the gathered data
is passed at initialization; Widgets in the DataDialog are populated
accordingly with the passed data, and the dialog is then shown modally to the 
User. Qt supports a specific exec() method on the dialog class to make this kind
of interaction extremely convenient.

With the dialog now visible, the User can modify the presented values, with 
validation performed on the Dialog class. Eventually, the User will issue
either an "Ok" or a "Cancel". With an "Ok", the new data is gathered from the
Dialog, processed by the backend and applied to match the changed options.
With "Cancel", the gathered information is simply discarded. 

This strategy is extremely effective for scenarios matching the conditions
above. Its major flaw is in testability, requiring automated interaction
with the widgets to test correct data transfer and validation.

Note: different from the Local Model. The Dialog contains the data and it's extracted by it.

# Design
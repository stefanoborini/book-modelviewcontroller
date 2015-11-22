# Data Dialog

### Motivation

Data Dialog is a simplified design to retrieve information from the User,
as in the case of Preference dialogs.
Constraints for the application of this pattern are the following:

 - The dialog must be Modal (i.e. when visible, interaction with the rest of the application is forbidden)
 - The dialog allows only Accept ("Ok" button) and Reject ("Cancel" button) strategies, not Apply.
 - It must not need to synchronize with change of status of the application that may occur while the Data Dialog is visible.

Data Dialog is extremely effective on the client side when the above scenario applies
Its major flaw is in testability of the Data Dialog itself. Client code invoking the
Data Dialog is instead simplified in testability, being able to replace Data Dialog
with a mock honoring the same interface.

### Design

When shown, Data dialog is passed a Model object containing the relevant information.
This Model does not need to support notification, and can be a plain Dictionary. The show operation must be blocking on the invoking code.

Data Dialog extracts the information from the passed Model and populates its widgets accordingly.

  Next, a DataDialog object is instantiated, and the gathered data
is passed at initialization; Widgets in the DataDialog are populated
accordingly with the passed data, and the dialog is then shown modally to the 
User. Qt supports a specific exec() method on the dialog class to make this kind
of interaction extremely convenient.

With the dialog now visible, the User can modify the presented values, with 
validation performed on the Dialog class. Eventually, the User will issue
either an "Ok" or "Cancel". With an "Ok", the new data is gathered from the
Dialog, processed by the backend and applied to match the changed options.
With "Cancel", the gathered information is simply discarded. 

Alternative designs can return the changed information only, or 
let the client code extract the information from the dialog's widgets, although the latter is impractical.
information 
Note: different from the Local Model. The Dialog contains the data and it's extracted by it.

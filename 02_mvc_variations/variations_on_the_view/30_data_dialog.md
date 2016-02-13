# Data Dialog

### Motivation

Data Dialog is a simplified and practical design to retrieve information from the User
by means of a Dialog. It is generally used for Preference dialogs.

To use a Data Dialog, the following constraints must be respected:

 - It must be Modal (i.e. when visible, interaction with the rest of the application is prevented)
 - It only allows Accept (``Ok`` button) and Reject (``Cancel`` button) operations, not Apply.
 - It does not need to synchronize with the application state while visible.

Testability of the Data Dialog itself is potentially complex due to its synchronous nature.
Client code however can replace Data Dialog with a mock honoring the same interface,
resulting in easier testability of this part of the application.

This design is different from the Local Model.
A local model is a real Model that is connected to the View through notification,
but has simply been copied to preserve its older state in case the changes are
reverted. Data dialog, on the other hand, is simply a View with an API to
accept data to populate its widgets, or retrieve their content in a trivial
representation.

### Design

Data dialog's widgets are populated through an appropriate method call, passing
data with a trivial representation.
The Data Dialog ``show`` operation must be blocking on the invoking code.
Once invoked, Data Dialog extracts the information from the passed Model and
populates its widgets accordingly.

Next, a DataDialog object is instantiated, and the gathered data
is passed at initialization; Widgets in the DataDialog are populated
accordingly with the passed data, and the dialog is then shown modally to the
User.

With the dialog now visible, the User can modify the presented values, with
validation performed on the Dialog class. Eventually, the User will issue
either an "Ok" or "Cancel". With an "Ok", the new data is gathered from the
Dialog, processed by the backend and applied to match the changed options.
With "Cancel", the gathered information is simply discarded.

Alternative designs can return the changed information only, or
let the client code extract the information from the dialog's widgets, although
the latter is impractical.

### Practical Example

Qt supports a specific exec() method on the dialog class to make this kind
of interaction extremely convenient.

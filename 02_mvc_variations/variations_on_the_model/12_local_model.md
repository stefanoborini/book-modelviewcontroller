# Local Model

### Motivation

A common use case of GUI interaction is to spawn a dialog containing configuration options, and let the user apply (through an "Ok" button) or 
discard (through "Cancel") his changes.

A Local Model allows the above use case by letting the Dialog View operate 
on a copy of the Original Model. 
The copy can then be either discarded 
(if "Cancel" is clicked), or merged with the Original Model (if "Ok" 
is clicked). This approach guarantees that business rules of the Model 
are enforced observed while changes are made on the data.

# Design

Models needing support for this strategy generally implement:
- a `copy()` method (or similar), creating and returning a copy of 
  itself.
- an `update(local_model)` or `merge(local_model)` method, updating 
  the Original Model's data with the Local Model data.

When the Dialog is requested by a user operation, the Original Model is 
copied. This copy (Local Model) is passed as a Model to the Dialog. 
User's operations on the Dialog are applied to the Local Model, and 
these changes must not influence the rest of the application, meaning that listeners must not be copied.

If the user dismisses the Dialog with "Cancel", the Dialog is closed and the 
Local Model is simply discarded. When the user clicks on "Ok", 
the controlling code submits the Local Model to the Original Model 
via `update()`. Changes are verified and merged, and if actual changes 
exist the Original Model notifies its listeners.

Optionally, the View can also have a "Revert" button which either 
performs a merge in the opposite direction (Original onto Local) or 
simply discards the Local Model, creates a new copy, and sets the Dialog
to observe the new copy.


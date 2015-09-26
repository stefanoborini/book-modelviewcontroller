# Accumulator

### Motivation

Accumulator is a special variation of the Compositing Model where notifications
from the submodels are not propagated to the final listener, but are instead
recorded for later delivery. 
Like a Lazy Model, the Accumulator delivers the
recorded notifications when instructed from an external client.

The Accumulator is useful in the following circumstances:

- when multiple operations must be performed on a Model, and each operation
  would trigger a notification, forcing unnecessary refreshes of the View.
  The Accumulator neutralizes the chain of notifications, and can deliver a
  single notification at the end of the series of operations.

- when multiple Models have notification dependencies among themselves, but
  we want the client View to refresh only when all notifications 
  have propagated and the Models are in a consistent state.


accumulate notifications in a buffer, then send them out at the end of the transaction.

### Design

Views listen to the accumulator for notifications. The accumulator, on the other hand, listen to its submodels. When the submodels report a change, the accumulator records that a change has occurred, but does not propagate the notification to the View. Instead, it records that a change has happened.


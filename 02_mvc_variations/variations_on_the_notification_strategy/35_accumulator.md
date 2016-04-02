# Accumulator

### Motivation

Accumulator is a notification strategy used to prevent redundant delivery: when
changes are performed on the Model, the intended notification is not delivered
to the listeners. Instead, it is recorded once and kept for later delivery. 
Redundant notifications are discarded. Like in a Lazy Model, the Accumulator
then delivers the recorded notifications when instructed from an external
request.

The Accumulator is useful in the following circumstances:

- when multiple operations must be performed on a Model, and each operation
  would trigger a notification, forcing unnecessary refreshes of the View.
  The Accumulator neutralizes redundant notifications, and delivers a
  single notification at the end of the series of operations.

- when multiple Models have notification dependencies among themselves, but
  we want the client View to refresh only when all notifications 
  have propagated and the Models are in a consistent state.

### Design

The accumulator can exist in two different forms: either as a native Model accumulator,
or as an ``External Accumulator``.

A native Model Accumulator is a Model whose design allows storing notifications
in a private log, instead of issuing them. Additional notifications are added
only if a similar entry is not already present in the log, although for some
qualified notifications some notification merging is needed. For example, if a
Model incurs two changes and the notification contains qualifying information
about the change, the following scenario would occur:

1. The Model ``value_a`` is requested to change from 3 to 5. A notification is
   added to the log as ``{ "change" : "value_a", "old_value" : 3, "new_value" : 5}``
2. The Model `value_a`` is requested to change again from 5 to 7. 
   A notification for the change of ``value_a`` is already present in the log, but the
   new notification cannot be simply discarded.
3. The Model combines the old notification and the new notification so that the log contains
   the original value (3), and the latest (7) ``{ "change" : "value_a",
   "old_value" : 3, "new_value" : 7}``
 
On external client request, the Model will then consume the log and deliver the notifications.

The second accumulator strategy, the ``External Accumulator`` is instead providing
accumulator features to one or more SubModels not supporting the concept natively. 
The Accumulator listen to its SubModels and logs their notifications. The View is
listening to the Accumulator and therefore is not informed of the changes. 

Depending on the surrounding design choices, 

1. additional notifications from any submodel are neutralized.
2. additional notifications from the same submodel are neutralized. notifications from other submodels are recorded.
3. all notifications are enqueued.


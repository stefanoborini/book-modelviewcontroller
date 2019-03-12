---
parent: Advanced MVC
summary: Prevent recursive notifications to propagate
nav_order: 11
---
# Notification looping prevention

Notification messages from the Model can become problematic for a series of
reason

- the Views get informed that changes occurred, but it's in a part of the
  data model that is not represented by a specific View. Views must go through a
  refresh cycle even if no data has changed for them
- A sequence of changes is performed on the Model, forcing a refresh of all the
  Views at each change, while a single refresh at the end of the sequence would
  suffice.
- The update-change cycle lead to an infinite loop

Consider the following case of a SpinBox containing the value 3, and the associated Model value currently set to 3 as well. When the user interacts with the SpinBox, clicking the up arrow, the following sequence of events occurs:

1. a valueChanged() signal is issued by the SpinBox with the new value, 4. We assume the SpinBox keeps showing the old value, as it represents the Model, which at the moment contains 3. 
2. the Controller.setValue(4) method is called, which in turn calls Model.setValue(4).
3. the Model stores the new value 4, then issue a _notifyListeners to inform all the connected views, including the SpinBox.
4. the SpinBox receives the notify(), which now fetches the new value from the Model and sets the new value using QSpinBox.setValue(4)
5. the SpinBox is still containing the value 3. QSpinBox.setValue(4) triggers valueChanged() again.
6. Controller.setValue is called again, reproducing the situation at point 2.

With this scenario, the application is potentially entering a notification
loop. A prevention strategy is to have the Model notify the listeners only if
the new value differs from the currently stored one. This solution will
terminate at point 3, technically performing useless Controller.setValue and
Model.setValue calls.  A tempting alternative solution is to have the SpinBox
increment its visualized value independently from the Model, thus having the
View autonomous in its visualized state.  With this approach, after step 1 the
SpinBox will show the number 4. The chain of events will unfold exactly in the
same way until step 4. The SpinBox will now observe that the new value in the
Model is the same as the one it is currently displaying, terminating the chain
by not triggering a valueChanged().  Depending on the toolkit used, graphical
Views may or may not behave as described, but the fundamental issue with this
approach is that the View is assuming to know the next value, and setting it
accordingly, without involving any logic from the Controller or Model. The
Model could, for example, consider the new value 4 to be invalid and set itself
to the next valid one, for example 27. This will force the View to update its
graphical representation again. 

Another strategy is to prevent the View from updating itself twice within the
same cycle of events. A possible implementation of this strategy is to hold a
flag updating on the View. The flag is set to True at step 1. The chain of
events develops in the same way until step 5, where the setValue operation will
check for the flag. If true, it will only update the graphical aspect of the
widget, and skip the triggering of the second valueChanged() signal.  Another
strategy is to have a View that does not triggers valueChanged under certain
conditions. 

Shut down the Model notification system? not a good idea. other parties will
not receive events.  Another alternative is to detach the View from the
notification. It will not receive update notifications from the model, just set
the value. It won't see changes in the model that originate from outside
though.


To prevent notification trashing, one can rely on transaction, to
turn off notifications on the model, perform a set of changes, then
triggering the notification by closing the transaction.  When
multiple independent modifications must be performed on the model in
sequence, it pays off to have a method to disable and enable
notifications. Without this technique, every individual change would
trigger an update and force a refresh of the connected views,
potentially ruining performance and exposing the user to progressive
changes through the interface as each change is applied. By
disabling the notifications, performing the changes, and re-enabling
the notifications, a single update will be triggered.  model packing
multiple changes to deliver a single refresh to the view controller
disabling notifications of the model.

FIXME: 
Another example:

a view has two methods, one that stores stuff on the model from the widget
content, and another one that takes data from the model and stores it in
the widgets. If the widget.setValue(model.value) triggers a notification and a request for syncing
(as normally happens when the user writes a value), we need to disable
notification when the modelToWidget() method is called, otherwise it will trigger
notifications into the model, potentially calling modelToWidget() again.

We normally skip this with a flag in the  modelToWidget() method that prevents recursion
by bailing out if set to true, and it's set to true immediately, or disabling notification
for the widget to synchronize.
Make a code example for this


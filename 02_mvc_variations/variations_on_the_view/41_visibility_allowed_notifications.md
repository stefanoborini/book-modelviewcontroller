# Visibility Allowed Notifications

### Motivation

Views that are hidden to the User generally do not need to be notified 
of Model changes: depending on the nature of the View, this can result in
performance degradation from mild to severe. Machine cycles can be saved 
by ignoring the notification altogether.

When the View becomes visible again, synchronization with the Model must occur, 
but only if an actual change has taken place. Failure to do so would slow down the
return of the View without reason.

### Design

When a notification is delivered to the View, the View checks for its visibility.
If not visible, it simply sets a `needs_update` flag.

When the View is made visible again, and assuming the View preserves
its visual state even when hidden, the `needs_update` flag is checked. 
If the flag is set, the View resynchronizes against the Model contents,
otherwise, it just presents the old visual appearance.

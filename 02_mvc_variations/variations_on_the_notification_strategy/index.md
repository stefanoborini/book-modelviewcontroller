# Variations on the notification strategy

   * [Qualified Notification](qualified_notification.md): Deliver notification with enhanced semantics to inform listeners about what has changed.
   * [Qualified Notification Model with Subscribing](qualified_notification_model_with_subscribing.md): View subscribes to specific events and gets notified only when they occur.
   * [Passive Model](passive_model.md): A Model without notification features.
   * [Lazy Model](lazy_model.md): A Model delivering its notifications on explicit request.
   * [Accumulator](accumulator.md): Listens to submodels and squashes multiple notifications into a single one.
   * [Pre/Post notification](pre_post_notification.md): Deliver notifications before or after the change.
   * [Vetoers](vetoers.md): Inquire listeners to approve or deny a change to occur.
   * [Signals](signals.md): Isolate notification into a separate object.
   * [Multiple Notification Entry Points](multiple_notification_entry_points.md): Notifications can be delivered to arbitrary methods.

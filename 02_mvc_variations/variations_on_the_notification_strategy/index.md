# Variations on the notification strategy

   * [Qualified Notification](qualified_notification.md): Deliver notification with enhanced semantics to inform listeners about what has changed.
   * [Qualified Notification Model with Subscribing](qualified_notification_model_with_subscribing.md): View subscribes to specific events and gets notified only when they occur.
   * [Passive Model](07_passive_model.md): A Model without notification features.
   * [Lazy Model](lazy_model.md): A Model delivering its notifications on explicit request.
   * [Accumulator](35_accumulator.md): Listens to submodels and squashes multiple notifications into a single one.
   * [Delayed Model](40_delayed_model.md): Neutralizes fast notifications through a timeout.
   * [Throttling](41_throttling.md): Neutralizes fast notifications, but issue a change immediately.
   * [Pre/Post notification](47_pre_post_notification.md): Deliver notifications before or after the change.
   * [Vetoers](48_vetoers.md): Inquire listeners to approve or deny a change to occur.
   * [Signals](49_signals.md): Isolate notification into a separate object.
   * [Request for Interest](60_request_for_interest.md): The Model notifies the listeners only if they must actually react to the change.
   * [Multiple Notification Entry Points](multiple_notification_entry_points.md): Notifications can be delivered to arbitrary methods.

Visibility Allowed Notifications
--------------------------------

An interesting optimization for the View is that it can prevent
refreshing if not visible. When not visible, instead of performing
potentially elaborate operations in response to the modified model,
the view can simply set a flag.

When the view is made visible again (and we assume the view preserves
its visual state even when hidden), the flag is checked. If the flag has been
modified, it means that the model and the View are not synchronized and the View has to
perform the refresh. Otherwise, it just presents the old visual appearance.

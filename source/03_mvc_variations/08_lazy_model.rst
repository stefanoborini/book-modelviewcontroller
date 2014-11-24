Lazy Model
----------

The passive model doesn't notification. The active model does notification every time there's a change.
In-between these two, there's the Lazy Model. The lazy model does not perform notifications,
but holds the list of interested listeners. When some external factor pokes the lazy model,
it notifies its listeners.

A lazy model is a good strategy when we want to retain full control on the notification flow as 
in the passive model, but at the same time we want to keep the observers centralized on the model.



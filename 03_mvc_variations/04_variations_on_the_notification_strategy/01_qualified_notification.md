---
grand_parent: MVC Variations
parent: Variations on the notification strategy
nav_order: 1
---
# Qualified Notification

### Motivation

The most basic form of Model notification is unqualified: Views are
just informed that a change occurred in the Model state. In response, 
Views retrieve the new Model state and repaint themselves accordingly. 
This approach is simple but coarse. Consider these scenarios:

- A specific View is only interested in a subset of the Model. 
  The Model changes, but not in the data relevant to the View.
  The View is forced to repaint even if none of the data
  it displays actually changed

- A View has additional state which is destroyed by a full repaint.
  For example, a TreeView representing files in a directory keeps state 
  for the opened/closed sub-branches. If a new file is added and the View
  is forced to rescan and repaint, the open/closed state is discarded.
  Knowing the nature of the change would help in handling this case.

- A View takes a very long time to perform a repaint from the full
  Model's content, but it can run faster if it can operate by knowing 
  only the change.

A Qualified Notification addresses the above cases by enhancing the 
notification system with a more fine-grained protocol carrying information
about what has changed in the Model. 

### Design

Qualified Notification can be implemented by passing arguments to the Views' 
``notify()`` method. When the Model changes and calls this method on the
subscribed Views, it passes information about

- The subject of the change (*e.g.*, which Model property has changed)
- The nature of the change (*e.g.*, the previous and new values)

The following example implementation trivially satisfies the above design

```python
class View():
    def notify(self, name, old_value, new_value):
        # ...
```

Unfortunately, this solution does not allow to notify about more than one
property change at a time. Additionally, it does not support multiple Models
notifying the same View, as the View would not be able to differentiate which
Model is reporting the change.

A more flexible approach is given by the following implementation

```python
class View():
    def notify(self, change_info):
        # ...
```

where ``change_info`` is a dictionary or other data object describing the
change in enhanced detail. Models are responsible for creating and populating 
this data object so that is meaningful to the receiving View. As a side effect
of the design, the View does not need to inquire the Model's state anymore.
Instead, it keeps its synchronization by means of the change information.

Most modern MVC frameworks provide qualified notifications in one form or another (e.g.
bound properties or signals). An unqualified reporting is uncommon but not completely 
dismissable as a strategy, especially for cases where there is no granularity in the 
Model to be exploited, or the View cannot take advantage of a fine-level notification.

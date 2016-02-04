# Qualified Notification Model

### Motivation

The most basic form of Model notification just informs the listeners that 
a change occurred in its state. In response, Views retrieve the new Model
state and repaint themselves accordingly. This approach is simple, but 
often too coarse and wasteful. Consider these scenarios:

- A specific View is only interested in a subset of the Model. 
  The Model changes, but not in the data relevant to the View.
  The View is forced to repaint even if none of the data
  it displays actually changed

- A View has additional state which is destroyed by a full repaint.
  For example, a TreeView representing files in a directory keeps state 
  for the opened/closed sub-branches. If a new file is added and the View
  is forced to rescan and repaint, the open/closed state is discarded.

- A View takes a very long time to perform a repaint from the full
  model's content, but it can run faster if it can operate by knowing 
  only the change.

These cases demonstrate how an unqualified notification can be wasteful
or damage the quality of the user interaction.

A Qualified Notification is a possible solution to the above
scenarios. It enhances the notification system with a more fine grained
protocol carrying information about what has changed in the Model. 

### Design

Qualified Notification can be implemented by passing arguments to the Views' 
``notify()`` method. When the Model changes and calls this method on the
subscribed Views, it passes information about

- The subject of the change (for example, which Model property has changed)
- The nature of the change (for example, the previous and new values)

The following example implementation trivially satisfies the above design

```python
class View():
    def notify(self, name, old_value, new_value):
        # ...
```

but unfortunately restricts the protocol to a single property change.
It also cannot support multiple Models notifying the same View, as the View
would not be able to differentiate which Model is reporting the change.

A more flexible approach is given by the following example:

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

The resulting design allows a more refined handling of Model changes. Views 
can skip a refresh cycle if the Model change does not affect the visual 
appearance, or apply the change information only to the relevant parts of its
visual state, resulting in improved UI performance.


### Additional comments


Alternatively, fragment the Model into two model objects, so
that the View can connect only to the part that is relevant.


Advantages: 
 - the data update object may contain logic on how to present itself on the views, especially if this rendering is trivial (e.g. pure text)
 - if the model is on another thread, it pushes and forces the refresh of the view. In the traditional case, the view may lag behind.

Disadvantages:
 - transfer stuff that may be useless for that specific view. The view may then subscribe for specific data and receive only those in the data update object


Notification granularity

notifications can have different levels of granularity. The coarse level is that the model reports
it changed, and let the View synchronize against the new data. Simple, but can become a bottleneck if
the redraw is forced even when data that are not displayed are modified. Also, the model gives no information
about what changed, which means that the view must either throw its whole state away and reset it anew,
or do a proper merge of all the data involved. This may create problems when visual state may be lost
(e.g. if an entry is open or close in a tree view)

a fine grained mechanism, where individual properties report their change.
(e.g. bound properties in javabean) Problem when multiple
properties must be changed in sequence, as they would trigger multiple useless
notifications. 

a qualified notification mechanism that gives details of the changeset.
e.g. old value/new value
- if at initialization or not
- if before or after the change


Add a note on the fact that if the model pushes information, then this
information characteristics falls on the signature of the notifyObserver()
methods. So, its signature must be somehow generic. The model pretends to know
what the view is specifically interested in, something it might not know, so it
must simply send itself, and let the view go through it, or have a protocol to
specify what changed.


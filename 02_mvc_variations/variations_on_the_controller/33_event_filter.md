# Event Filter

### Motivation

An Event Filter is a special kind of Controller that intercepts UI events 
before they are delivered to the View. The gained additional flexibility
allows to handle specific events differently than the standard response
provided by the View, or to suppress some events so that they never reach
the View.

### Design

Event Filters can be either objects with a specific interface, or function objects 
with a signature accepting the event. Views provide an interface to set and unset 
them. When the View receives an event, its implementation first routes
the event toward the Event Filter, which is free to respond acting on Models, 
Views or Controller objects. These objects may or may not be known by the View.

Once the Event Filter completes its execution, it communicates to the View if
the event should be processed as usual or not. In the latter case, the View
acts as if the event never occurred.

The interaction diagram explains the design in more concrete terms

<p align="center">
    <img src="images/event_filter/event_filter.png">
</p>

1. Events are routed into the Filter by the View, through a ``handle_event(event)`` interface
2. The Event Filter can now recognize a specific event and perform operations on the
   Models it is connected to. These Models may or may not be the same that the View is 
   observing.
3. If the Event Filter handles the Event, The View is notified through either a flag on 
   the Event class or a boolean return value for the ``handle_event()`` method. In the 
   case presented above, the latter strategy is used. The ``True`` return value implies
   that the event should not be handled further by the View.
4. If ``EventFilter.handle_event()`` returns ``False``, the View handles the event as usual.
   
Please observe that the Event Filter might choose to handle the event and still
return ``False``, allowing the View to operate as usual.

As a consequence of its design and purpose, the Event Filter must be dependent on
the UI, and must know how to handle the UI Event interface. 

### Practical Example

The Qt toolkit offers a clear example of an Event Filter. A class ``EventFilter``
derived from ``QObject`` reimplements the method ``QObject.eventFilter()``. 
An instance of ``EventFilter`` is then installed onto a target object through ``installEventFilter()``. 

The following program illustrates the concept

```python
import sys
from PySide import QtGui, QtCore
app = QtGui.QApplication(sys.argv)

class EventFilter(QtCore.QObject):
    def eventFilter(self, receiver, event):
        print(type(receiver), type(event))
        return False
        
event_filter = EventFilter()
button = QtGui.QPushButton("hello")
button.installEventFilter(event_filter)
button.show()

app.exec_()
```

The example creates a `QPushButton` and installs an `EventFilter` instance on it.
UI events (mouse movements and clicks, key presses, show/hide, resize, repaint etc.)
that are meant for the `QPushButton` are first dispatched to `EventFilter.eventFilter()`,
then to the `QPushButton` if and only if the `eventFilter` method returns `False`

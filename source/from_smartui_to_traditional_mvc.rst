1. From Smart-UI to Traditional MVC
===================================

Smart-UI: A single class with many responsibilities
---------------------------------------------------

We start this exploration of MVC with the most trivial and simplistic
application: a click counter. This application shows a button with a number.
The number is increased every time the button is clicked. 
    
.. image:: _static/images/SmartUI.png
   :align: center

We can implement this application as follows:

::

    import sys
    from PyQt4 import QtCore, QtGui

    class Counter(QtGui.QPushButton):
        def __init__(self, \*args, \*\*kwargs):
            super(Counter, self).__init__(\*args, \*\*kwargs)
            self._value = 0
            self._update()

        def mouseReleaseEvent(self, event):
            super(Counter, self).mouseReleaseEvent(event)
            self._value += 1
            self._update()

        def _update(self):
            self.setText(unicode(self._value))

    app = QtGui.QApplication(sys.argv)
    counter = Counter()
    counter.show()
    app.exec_()

The application's main and only visual component, Counter, is derived from a
single GUI class, a Qt QPushButton. The Counter class holds multiple
responsibilities: 

    1. Stores the current click count value in the member variable self._value. 
    2. Handles the logic that modifies self._value. Every time the button is
       clicked, Qt invokes  mouseReleaseEvent automatically. In this method the click
       counter is incremented.
    3. Synchronizes the aspect of the button with the current self._value, by invoking setText.

Combining these three responsibilities into a single class gives us the so
called Smart-UI design. While appealing for its simplicity and compactness,
this design does not scale well to larger applications, where state, user
events and graphic layout are more complex and intertwined, and need to change
often. In particular, we can observe the following issues with the current
design, as we imagine to scale it up:

Access and modification of the current value from outside is cumbersome, being
contained into an all-encompassing visual object: external objects that want to
modify the current counter need to make sure that the represented value is
synchronized.

It is difficult for multiple visual objects to visualize the same information,
maybe with two different visual aspects (e.g. both as a counter and as a
progress bar)

The logic dealing with visual aspect (i.e. handling and layouting widgets,
updating the label on the button), interaction aspect (handling the user
initiated mouse click to perform the increment operation) and business aspect
(incrementing the counter) are of different nature, and would be better kept
separated. This would ease testability, simplify code understanding and
interaction.


Document-View: dividing state from GUI
--------------------------------------

*Additional Need*: Represent the same information in two visual forms at the same time.

To solve the shortcomings of Smart-UI, we take advantage of the intrinsic
division into visual, interaction and business role expressed by a GUI
application. In Smart-UI, these three roles happen to be assigned to the same
class, but we can reorganize our code so that they are kept separated. The
resulting design is a two-class system known in literature as Document-View or
Model-Delegate.  The first step is to partition out the data, represented by
the self._value variable, into a separate class Document. For our system to
continue to work, the visual part View must now be informed of changes to this
data. The Document will therefore not only hold self._value, but also provide
an interface to query and modify this data and a strategy to notify other
objects when changes occur. This is expressed in the following implementation
code:

::

    class CounterDocument(object): 
        def __init__(self): 
            self._value = 0 
            self._listeners = set() 

In addition to the value, the self._listeners member variable holds references
to external objects interested in being notified about changes. We use a python
set instead of a list to prevent accidental registration of the same object
twice. Interested objects can register and unregister through the following
methods

::

    def register(self, listener): 
        self._listeners.add(listener) 
        listener.notify() 

    def unregister(self, listener): 
        self._listeners.remove(listener) 


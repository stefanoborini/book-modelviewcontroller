#!/usr/bin/env python
# traditional
# Example of Traditional MVC. By Stefano Borini 2013. CC-SA
# NOTE: Not using Qt features (signal/slots) on purpose.

import sys
from PyQt4 import QtCore, QtGui


class Model(object):
    def __init__(self):
        # Initializes the model data.
        self._value = 0

        # Create a set to hold the interested listeners.
        # Observe how the model is not aware of the controller,
        # and aware of the view(s) as registered listener(s).
        # It does not know anything about the view interface,
        # except for the method .notify()
        self._listeners = set()

    def setValue(self, value):
        # Sets the value in the model, and if needed, reports the change to the listeners.

        if value != self._value:
            # We want to notify for change only if there's an actual change
            self._value = value
            self._notifyListeners()

    def value(self):
        # returns the currently stored value
        return self._value

    def register(self, listener):
        # Interface for observer pattern.
        # The view registers itself on the model to receive notifications
        # In Qt, this mechanism can be replaced with signal/slot, further
        # decoupling model from views and allowing a completely oblivious model.
        self._listeners.add(listener)

        # When the listener registers itself, we immediately tell it
        # there's something worth of its attention
        listener.notify()

    def unregister(self, listener):
        # Not used here, but generally useful to have. Unregisters a listener
        self._listeners.remove(listener)

    def _notifyListeners(self):
        # Here we broadcast to all listeners that a change occurred and
        # they should update themselves. Note that the model knows only the
        # notification interface of the view, nothing more.
        for l in self._listeners:
            l.notify()

class View(QtGui.QPushButton):
    def __init__(self, model):
        super(View, self).__init__()
        self._model = None
        self._controller = Controller(self)
        self._model = model
        self._controller.setModel(model)
        self._model.register(self)

    def mouseReleaseEvent(self, event):
        # The GUI action is interpreted here, called automatically by the Qt Framework

        # Call the base class implementation
        super(View, self).mousePressEvent(event)

        # The view acts appropriately by calling the proper method on the controller
        self._controller.addOne()

    def notify(self):
        # When a change in the model occurs, this method gets called, so that the view
        # can act appropriately and refresh itself with the new value
        self.setText(unicode(self._model.value()))

class Controller(object):
    def __init__(self, view):
        # The controller needs references to the model and the view
        self._view = view
        self._model = None

    def setModel(self, model):
        self._model = model

    def addOne(self):
        # The controller performs the operation on the model according to the
        # semantic of the method, that is, to add one to the model data.
        # This is determined by the user action in the view, and called by it
        if self._model:
            self._model.setValue(self._model.value()+1)

app = QtGui.QApplication(sys.argv)

# Initialize
model = Model()
view = View(model)

# Show the view and exec the event loop
view.show()
app.exec_()

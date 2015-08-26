#!/usr/bin/env python
# traditional
# Example of Traditional MVC. By Stefano Borini 2013. CC-SA
# NOTE: Not using Qt features (signal/slots) on purpose.

import sys
from PyQt4 import QtCore, QtGui


class Model(object):
    def __init__(self):
        self._value = 0
        self._listeners = set()

    def setValue(self, value):
        print "Model.setValue ", value
        if value != self._value:
            self._value = value
            self._notifyListeners()

    def value(self):
        print "Model.value ", self._value
        return self._value

    def register(self, listener):
        self._listeners.add(listener)
        listener.notify()

    def unregister(self, listener):
        self._listeners.remove(listener)

    def _notifyListeners(self):
        print "Model._notifyListeners"
        for l in self._listeners:
            l.notify()

class View(QtGui.QSpinBox):
    def __init__(self, *args, **kwargs):
        super(View, self).__init__(*args, **kwargs)
        self._model = None
        self._controller = Controller(self)
        self.connect(self, QtCore.SIGNAL("valueChanged(int)"), self._controller.setValue)

    def setModel(self, model):
        if self._model:
            self._model.unregister(self)

        self._model = model
        self._controller.setModel(model)
        self._model.register(self)

    def notify(self):
        print "View.notify"
        self.setValue(self._model.value())

class Controller(object):
    def __init__(self, view):
        self._view = view
        self._model = None

    def setModel(self, model):
        self._model = model

    def setValue(self, value):
        print "Controller.setValue ", value
        if self._model:
            self._model.setValue(value*2)

app = QtGui.QApplication(sys.argv)

# Initialize
model = Model()
view = View()
view.setModel(model)

# Show the view and exec the event loop
view.show()
app.exec_()

#!/usr/bin/env python

import sys
from PySide import QtCore, QtGui


class Model(object):
    def __init__(self):
        self._password = None
        self._listeners = set()

    def getPassword(self):
        if self._password is None:
            password, ok = QtGui.QInputDialog.getText(None, "", "Password:", QtGui.QLineEdit.Password)
        self._password = password
        return self._password

    def clear(self):
        self._password = None
        self._notifyListeners()

    def register(self, listener):
        self._listeners.add(listener)
        listener.notify()

    def unregister(self, listener):
        self._listeners.remove(listener)

    def _notifyListeners(self):
        for l in self._listeners:
            l.notify()

class View(QtGui.QPushButton):
    def __init__(self, model):
        super(View, self).__init__()
        self._model = model
        self._model.register(self)

    def mouseReleaseEvent(self, event):
        super(View, self).mouseReleaseEvent(event)
        self._model.clear()

    def notify(self):
        self.setText(self._model.getPassword())

app = QtGui.QApplication(sys.argv)

# Initialize
model = Model()
view = View(model)

# Show the view and exec the event loop
view.show()
app.exec_()

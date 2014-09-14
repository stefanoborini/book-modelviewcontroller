from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt

class AddressBookView(QtGui.QListWidget):
    def __init__(self, model=None, *args, **kwargs):
        super(QtGui.QListWidget, self).__init__(*args, **kwargs)
        if model is not None:
            self._model = model
            self._model.register(self)

    def notify(self):
        self.clear()
        for i in range(self._model.numEntries()):
            entry = self._model.getEntry(i)
            string = "%s (%s)" % (entry["name"], entry["phone"])
            self.addItem(string)

    def setModel(self, model):
        self._model = model
        self._model.register(self)


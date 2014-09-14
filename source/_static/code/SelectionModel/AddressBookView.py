from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt

from ListWidget import ListWidget

def randomName():
    import random
    return random.choice(["Foo", "Bar", "Baz"])

class AddressBookView(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(QtGui.QWidget, self).__init__(*args, **kwargs)
        self._initUI()
        self._model = None
        self._selection_model = None

    def _initUI(self):
        self._layout=QtGui.QVBoxLayout()
        self.setLayout(self._layout)
        self._list_widget = ListWidget(parent=self)
        self._list_widget.itemSelectionChanged.connect(self.itemSelectionChangedSlot)
        self._layout.addWidget(self._list_widget)

        self._add_entry_button = QtGui.QPushButton("Add entry", parent=self)
        self._add_entry_button.clicked.connect(self.addEntryClicked)
        self._layout.addWidget(self._add_entry_button)

        self._remove_entry_button = QtGui.QPushButton("Remove entry", parent=self)
        self._remove_entry_button.clicked.connect(self.removeEntryClicked)
        self._layout.addWidget(self._remove_entry_button)

    def addEntryClicked(self):
        self._model.addEntry(name=randomName(), phone="12345" )

    def removeEntryClicked(self):
        print "remove"

    def itemSelectionChangedSlot(self, index, selected):
        print "itemSelectionChangedSlot ", index, selected
        self._selection_model.setSelected(index, selected)

    def notify(self, notifier):
        if notifier is self._model:
            self._list_widget.clear()
            for i in range(self._model.numEntries()):
                entry = self._model.getEntry(i)
                string = "%s (%s)" % (entry["name"], entry["phone"])
                self._list_widget.addItem(string)

        if notifier is self._model or notifier is self._selection_model:
            for i in range(self._model.numEntries()):
                self._list_widget.setItemSelected(i, self._selection_model.isSelected(i))

    def setModels(self, model, selection_model):
        self._model = model
        self._selection_model = selection_model
        self._model.register(self)
        self._selection_model.register(self)

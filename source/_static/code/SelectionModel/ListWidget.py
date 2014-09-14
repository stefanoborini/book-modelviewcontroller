from PyQt4 import QtGui, QtCore

class ListWidget(QtGui.QListWidget):
    itemSelectionChanged = QtCore.pyqtSignal(int, bool, name='itemSelectionChanged')

    def __init__(self, *args, **kwargs):
        super(ListWidget, self).__init__(*args, **kwargs)
        self.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)

    def selectionChanged(self, selected, deselected):
        super(ListWidget, self).selectionChanged(selected, deselected)

        for index in selected.indexes():
            self.itemSelectionChanged.emit(index.row(), True)
        for index in deselected.indexes():
            self.itemSelectionChanged.emit(index.row(), False)

    def setItemSelected(self, index, selected):
        self.item(index).setSelected(selected)

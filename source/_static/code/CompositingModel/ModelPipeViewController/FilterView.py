from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt

from FilterController import FilterController

class FilterView(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(QtGui.QWidget, self).__init__(*args, **kwargs)
        self._initGUI()
        self._model = None
        self._controller = FilterController(self._model, self)
        self.connect(self._filter_lineedit, QtCore.SIGNAL("textChanged(QString)"), self._controller.applyFilter)

    def _initGUI(self):
        self._hlayout = QtGui.QHBoxLayout(self)
        self.setLayout(self._hlayout)
        self._filter_label = QtGui.QLabel("Filter", parent=self)
        self._hlayout.addWidget(self._filter_label)
        self._filter_lineedit = QtGui.QLineEdit(parent=self)
        self._hlayout.addWidget(self._filter_lineedit)

    def setModel(self, model):
        self._model = model
        self._controller.setModel(model)

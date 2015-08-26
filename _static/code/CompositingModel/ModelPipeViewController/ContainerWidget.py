from PyQt4 import QtCore, QtGui

from FilterView import FilterView
from AddressBookView import AddressBookView

class ContainerWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(ContainerWidget, self).__init__(*args, **kwargs)
        self.filterview = FilterView(parent=self)
        self.addressbookview = AddressBookView(parent=self)
        self._vlayout = QtGui.QVBoxLayout()
        self.setLayout(self._vlayout)
        self._vlayout.addWidget(self.filterview)
        self._vlayout.addWidget(self.addressbookview)

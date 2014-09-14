#!/usr/bin/env python
# ProxyModel
# By Stefano Borini 2013. CC-SA

import sys
import os
from PyQt4 import QtCore, QtGui

from AddressBook import AddressBook
from AddressBookView import AddressBookView
from SelectionModel import SelectionModel

app = QtGui.QApplication(sys.argv)

address_book = AddressBook()
selection_model = SelectionModel(address_book)
view1 = AddressBookView()
view1.setModels(address_book, selection_model)
view2 = AddressBookView()
view2.setModels(address_book, selection_model)
view1.show()
view2.show()
app.exec_()

#!/usr/bin/env python
# ProxyModel
# By Stefano Borini 2013. CC-SA

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Common"))
from PyQt4 import QtCore, QtGui

from AddressBookCSV import AddressBookCSV
from AddressBookXML import AddressBookXML
from AddressBook import AddressBook

from AddressBookView import AddressBookView

app = QtGui.QApplication(sys.argv)

csv1_model = AddressBookCSV("../Common/file1.csv")
xml_model = AddressBookXML("../Common/file.xml")
csv2_model = AddressBookCSV("../Common/file2.csv")

address_book = AddressBook([csv1_model, xml_model, csv2_model])

view = AddressBookView(address_book)

view.show()
app.exec_()

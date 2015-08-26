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
from AddressBookFilter import AddressBookFilter
from AddressBookSorter import AddressBookSorter
from AddressBookView import AddressBookView
from ContainerWidget import ContainerWidget

# Application startup
app = QtGui.QApplication(sys.argv)

# Initialize the Models
csv1_model = AddressBookCSV("../Common/file1.csv")
xml_model = AddressBookXML("../Common/file.xml")
csv2_model = AddressBookCSV("../Common/file2.csv")

address_book = AddressBook([csv1_model, xml_model, csv2_model])
address_book_filter = AddressBookFilter(address_book)
address_book_sorter = AddressBookSorter(address_book_filter)

widget = ContainerWidget()
widget.addressbookview.setModel(address_book_sorter)
widget.filterview.setModel(address_book_filter)

# Show the views and exec the event loop
widget.show()
app.exec_()

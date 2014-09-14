#!/usr/bin/env python
# By Stefano Borini 2013. CC-SA

import xml.etree.ElementTree as ET
from BaseModel import BaseModel

class AddressBookXML(BaseModel):
    def __init__(self, filename):
        super(AddressBookXML, self).__init__()
        self._filename = filename

    def numEntries(self):
        try:
            tree = ET.parse(self._filename)
            root = tree.getroot()
            return len(root.findall("entry"))
        except:
            return 0

    def getEntry(self, entry_number):
        try:
            tree = ET.parse(self._filename)
            root = tree.getroot()
            entry = list(root.findall('entry'))[entry_number]
            return {'name': entry.find('name').text,
                    'phone': entry.find('phone').text
                    }
        except:
            raise IndexError("Invalid entry %d" % entry_number)

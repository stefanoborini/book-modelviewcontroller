#!/usr/bin/env python
# By Stefano Borini 2013. CC-SA

from BaseModel import BaseModel

class AddressBookCSV(BaseModel):
    def __init__(self, filename):
        super(AddressBookCSV, self).__init__()
        self._filename = filename

    def numEntries(self):
        try:
            return len(open(self._filename, "r").readlines())
        except:
            return 0

    def getEntry(self, entry_number):
        try:
            line = open(self._filename, "r").readlines()[entry_number]
            name, phone = line.split(',')
            return { 'name' : name.strip(), 'phone' : phone.strip()}
        except:
            raise IndexError("Invalid entry %d" % entry_number)

#!/usr/bin/env python
# By Stefano Borini 2013. CC-SA

from BaseModel import BaseModel

class AddressBook(BaseModel):
    def __init__(self):
        super(AddressBook, self).__init__()
        self._entries = []
        self._entries_id = {}
        self._last_id = 0

    def _newId(self):
        self._last_id += 1
        return self._last_id

    def numEntries(self):
        return len(self._entries)

    def getEntry(self, entry_number):
        return self._entries[entry_number]

    def addEntry(self, name, phone):
        new_id = self._newId()
        entry = { "id"    : new_id,
                  "name"  : name,
                  "phone" : phone
                }
        self._entries.append(entry)
        self._entries_id[new_id] = entry
        self._notifyListeners()

    def removeEntryById(self, entry_id):
        entry = self._entries[entry_id]
        self.entries.remove(entry)
        del self._entries[entry_id]
        self._notifyListeners()

    def currentIds(self):
        return self._entries_id.keys()

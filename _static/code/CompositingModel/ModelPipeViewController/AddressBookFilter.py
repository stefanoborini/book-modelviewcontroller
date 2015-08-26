from BaseModel import BaseModel

class AddressBookFilter(BaseModel):
    def __init__(self, model):
        super(AddressBookFilter, self).__init__()
        self._filter_string = ""
        self._model = model
        self._model.register(self)

    def numEntries(self):
        entries = 0
        for i in xrange(self._model.numEntries()):
            entry = self._model.getEntry(i)
            if self._filter_string in entry["name"]:
                entries += 1

        return entries

    def getEntry(self, entry_number):
        entries = 0

        for i in xrange(self._model.numEntries()):
            entry = self._model.getEntry(i)
            if self._filter_string in entry["name"]:
                if entries == entry_number:
                    return entry
                entries += 1

        raise IndexError("Invalid entry %d" % entry_number)

    def setFilter(self, string):
        self._filter_string = string
        self.notifyListeners()

    def notify(self):
        self.notifyListeners()

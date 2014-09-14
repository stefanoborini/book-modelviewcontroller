from BaseModel import BaseModel


class AddressBook(BaseModel):
    def __init__(self, models):
        super(AddressBook, self).__init__()
        self._models = models
        for m in self._models:
            m.register(self)

    def numEntries(self):
        return sum([m.numEntries() for m in self._models])

    def getEntry(self, entry_number):
        def accumulate(l):
            current_total = 0
            res = []
            for i in l:
                current_total += i
                res.append(current_total)

            return res
        accumulated = accumulate([m.numEntries() for m in self._models])
        source_idx = map(lambda x: x <= entry_number, accumulated).index(False)

        try:
            return self._models[source_idx].getEntry(entry_number-accumulated[source_idx])
        except:
            raise IndexError("Invalid entry %d" % entry_number)

    def addEntry(self, name, phone):
        try:
            rw_model = [x for x in self._models if not x.readOnly()][0]
        except:
            raise Exception("AddressBook is read-only")

        rw_model.addEntry(name, phone)

    def notify(self):
        self.notifyListeners()

from BaseModel import BaseModel
import operator

class AddressBookSorter(BaseModel):
    def __init__(self, model):
        super(AddressBookSorter, self).__init__()
        self._model = model
        self._model.register(self)
        self._rebuildOrderMap()

    def numEntries(self):
        return self._model.numEntries()

    def getEntry(self, entry_number):
        try:
            return self._model.getEntry(self._order_map[entry_number])
        except:
            raise IndexError("Invalid entry %d" % entry_number)

    def notify(self):
        self._rebuildOrderMap()
        self.notifyListeners()

    def _rebuildOrderMap(self):
        values = []
        for i in range(self._model.numEntries()):
            values.append( (i, self._model.getEntry(i)["name"]) )

        self._order_map = map(lambda x: x[0], sorted(values, key=operator.itemgetter(1)))

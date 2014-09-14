#!/usr/bin/env python
# By Stefano Borini 2013. CC-SA

import collections
from BaseModel import BaseModel

SELECTION_DEFAULT = False

class SelectionModel(BaseModel):
    def __init__(self, model):
        super(SelectionModel, self).__init__()
        self._selection = collections.defaultdict(lambda : SELECTION_DEFAULT)
        self._model = model
        self._model.register(self)

    def setSelected(self, entry_number, selected):
        entry = self._model.getEntry(entry_number)
        self._selection[entry["id"]] = selected
        print self._selection
        self._notifyListeners()

    def isSelected(self, entry_number):
        entry = self._model.getEntry(entry_number)
        return self._selection[entry["id"]]

    def notify(self, notifier):
        present_ids = self._model.currentIds()

        for id_ in self._selection.keys():
            if id_ not in present_ids:
                print "removing id", id_
                del self._selection[id_]


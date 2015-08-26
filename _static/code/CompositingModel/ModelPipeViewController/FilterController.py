class FilterController(object):
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def applyFilter(self, filter_string):
        if self._model:
            self._model.setFilter(str(filter_string))

    def setModel(self, model):
        self._model = model

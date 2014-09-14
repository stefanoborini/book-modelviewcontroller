import sys
from PyQt4 import QtCore, QtGui

class CounterModel(object):
    def __init__(self):
        self._value = 0
        self._listeners = set()

    def setValue(self, value):
        if value != self._value:
            self._value = value
            self._notifyListeners()

    def value(self):
        return self._value

    def register(self, listener):
        self._listeners.add(listener)
        listener.notify()

    def unregister(self, listener):
        self._listeners.remove(listener)

    def _notifyListeners(self):
        for l in self._listeners:
            l.notify()

class Counter(QtGui.QPushButton):
    def __init__(self, model):
        super(Counter, self).__init__()
        self._model = model
        self._model.register(self)

    def mouseReleaseEvent(self, event):
        super(Counter, self).mouseReleaseEvent(event)
        self._model.setValue(self._model.value()+1)

    def notify(self):
        self.setText(unicode(self._model.value()))

class ProgressBar(QtGui.QProgressBar):
    def __init__(self, model):
        super(ProgressBar, self).__init__()
        self._model = model
        self._model.register(self)
        self.setRange(0,100)

    def notify(self):
        self.setValue(self._model.value())

app = QtGui.QApplication(sys.argv)
model = CounterModel()
counter = Counter(model)
progress = ProgressBar(model)
counter.show()
progress.show()
app.exec_()

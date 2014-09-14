#!/usr/bin/env python
# Application / Domain Model
# Example of Traditional MVC. By Stefano Borini 2013. CC-SA
# NOTE: Not using Qt features (signal/slots) on purpose.

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt


# Base class for Model, handling notification
class BaseModel(object):
    def __init__(self):
        self._listeners = set()

    def register(self, listener):
        self._listeners.add(listener)
        listener.notify()

    def unregister(self, listener):
        self._listeners.remove(listener)

    def _notifyListeners(self):
        for l in self._listeners:
            l.notify()

# Domain model.
class Engine(BaseModel):
    def __init__(self):
        super(Engine, self).__init__()
        self._rpm = 0

    def setRpm(self, rpm):
        if rpm < 0:
            raise ValueError("Invalid rpm value")

        if rpm != self._rpm:
            self._rpm = rpm
            self._notifyListeners()

    def rpm(self):
        return self._rpm

    def isOverRpmLimit(self):
        return self._rpm > 8000

class DialViewModel(BaseModel):
    def __init__(self, engine):
        super(DialViewModel, self).__init__()
        self._dial_color = Qt.green
        self._engine = engine
        self._engine.register(self)

    def color(self):
        return self._dial_color

    def notify(self):
        if self._engine.isOverRpmLimit():
            self._dial_color = Qt.red
        else:
            self._dial_color = Qt.green

        self._notifyListeners()

class Dial(QtGui.QDial):
    def __init__(self, *args, **kwargs):
        super(Dial, self).__init__(*args, **kwargs)
        self._model = None
        self._view_model = None
        self._controller = DialController(self)
        self.connect(self, QtCore.SIGNAL("valueChanged(int)"), self._controller.changeRpm)
        self.setRange(0,10000)

    def setModels(self, model, view_model):
        if self._model:
            self._model.unregister(self)
        if self._view_model:
            self._view_model.unregister(self)

        self._model = model
        self._view_model = view_model
        self._controller.setModel(model)
        self._model.register(self)
        self._view_model.register(self)

    def notify(self):
        self.setValue(self._model.rpm())
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Button,self._view_model.color())
        self.setPalette(palette)

class DialController(object):
    def __init__(self, view):
        # The controller needs references to the model and the view
        self._view = view
        self._model = None

    def setModel(self, model):
        self._model = model

    def changeRpm(self, rpm):
        if self._model:
            self._model.setRpm(rpm)

class Slider(QtGui.QSlider):
    def __init__(self, *args, **kwargs):
        super(Slider, self).__init__(*args, **kwargs)
        self._model = None
        self._controller = SliderController(self)
        self.connect(self, QtCore.SIGNAL("valueChanged(int)"), self._controller.changeRpm)
        self.setRange(0,10)

    def setModel(self, model):
        if self._model:
            self._model.unregister(self)

        self._model = model
        self._controller.setModel(model)
        self._model.register(self)

    def notify(self):
        self.setValue(self._model.rpm()/1000)

class SliderController(object):
    def __init__(self, view):
        self._view = view
        self._model = None

    def changeRpm(self, value):
        if self._model is not None:
            self._model.setRpm(value*1000)

    def setModel(self, model):
        self._model = model


app = QtGui.QApplication(sys.argv)

# Initialize
engine = Engine()
view_model = DialViewModel(engine)

dial = Dial()
dial.setModels(engine, view_model)

slider = Slider()
slider.setModel(engine)

# Show the view and exec the event loop
dial.show()
slider.show()
app.exec_()

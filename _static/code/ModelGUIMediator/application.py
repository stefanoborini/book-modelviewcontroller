#!/usr/bin/env python
# Model GUI Mediator
# By Stefano Borini 2014. CC-SA

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt

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

class DialController(object):
    def __init__(self):
        self._view = None
        self._model = None

    def setModel(self, model):
        self._model = model
        self._model.register(self)

    def setView(self, view):
        self._view = view
        self._view.setRange(0,10000)
        self._view.connect(self._view, QtCore.SIGNAL("valueChanged(int)"), self.changeRpm)

    def changeRpm(self, rpm):
        if self._model:
            self._model.setRpm(rpm)

    def notify(self):
        if self._view:
            self._view.setValue(self._model.rpm())

class SliderController(object):
    def __init__(self):
        self._view = None
        self._model = None

    def setModel(self, model):
        self._model = model
        self._model.register(self)

    def setView(self, view):
        self._view = view
        self._view.setRange(0,10)
        self._view.connect(self._view, QtCore.SIGNAL("valueChanged(int)"), self.changeRpm)

    def changeRpm(self, rpm):
        if self._model:
            self._model.setRpm(rpm*1000)

    def notify(self):
        self._view.setValue(self._model.rpm()/1000)


# Application startup
app = QtGui.QApplication(sys.argv)

container = QtGui.QWidget()
layout = QtGui.QHBoxLayout()
engine = Engine()

dial = QtGui.QDial(container)
dial_controller = DialController()
dial_controller.setView(dial)
dial_controller.setModel(engine)

slider = QtGui.QSlider(container)
slider_controller = SliderController()
slider_controller.setView(slider)
slider_controller.setModel(engine)

container.setLayout(layout)
layout.addWidget(dial)
layout.addWidget(slider)

container.show()
app.exec_()

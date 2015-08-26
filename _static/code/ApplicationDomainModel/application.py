#!/usr/bin/env python
# Application / Domain Model
# By Stefano Borini 2013. CC-SA

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt

# Base class for Model, dealing with listeners and notification
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

# A class defining an Engine.
# This class contains pure Domain logic and state.
# It knows nothing about its representation on the GUI
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

# This is our application model, specifically the one that
# deals with the Dial-like representation of the engine rpm
# values. It must know GUI information that is strictly relevant
# to the widget representation it is going to expose.
# Note how it exports the same interface of the Domain model Engine,
# by passing through its query methods. Note additionally how it
# also listens to the Domain model for changes. When changes occur
# it modifies is state (the color), and reports changes itself.
class DialEngine(BaseModel):
    def __init__(self, engine):
        super(DialEngine, self).__init__()
        self._dial_color = Qt.green
        self._engine = engine
        self._engine.register(self)

    def dialColor(self):
        return self._dial_color

    def setRpm(self, rpm):
        self._engine.setRpm(rpm)

    def rpm(self):
        return self._engine.rpm()

    def notify(self):
        if self._engine.isOverRpmLimit():
            self._dial_color = Qt.red
        else:
            self._dial_color = Qt.green

        self._notifyListeners()

# One of our Views, specifically, the Dial-like rpm gauge.
# Its model is the Application-level model DialEngine
class Dial(QtGui.QDial):
    def __init__(self, *args, **kwargs):
        super(Dial, self).__init__(*args, **kwargs)
        self._model = None
        self._controller = DialController(self)
        self.connect(self, QtCore.SIGNAL("valueChanged(int)"), self._controller.changeRpm)
        self.setRange(0,10000)

    def setModel(self, model):
        if self._model:
            self._model.unregister(self)

        self._model = model
        self._controller.setModel(model)
        self._model.register(self)

    def notify(self):
        self.setValue(self._model.rpm())
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Button,self._model.dialColor())
        self.setPalette(palette)

# The controller for our dial class, receiving user actions on the dial
# to modify the rpms. Note how this controller again acts on the
# Application Model DialEngine.
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

# Another View with a slider-like interface. This View is different
# from the dial View because it acts on the Domain model. It would
# make no sense to act on the Application model, because it is tailored
# to the visual aspect of the Dial.
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

# The controller for the slider, acting on the Domain model to change the rpm.
class SliderController(object):
    def __init__(self, view):
        self._view = view
        self._model = None

    def changeRpm(self, value):
        if self._model is not None:
            self._model.setRpm(value*1000)

    def setModel(self, model):
        self._model = model


# Application startup
app = QtGui.QApplication(sys.argv)

# Initialize the Domain Model
engine = Engine()

# Initialize the Application Model for the Dial
gui_engine = DialEngine(engine)

# Setup the Dial view and pass its Application model
dial = Dial()
dial.setModel(gui_engine)

# Setup the slider and pass the Domain model
slider = Slider()
slider.setModel(engine)

# Show the views and exec the event loop
dial.show()
slider.show()
app.exec_()

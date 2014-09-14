#!/usr/bin/env python
# Model View Adaptor
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

# Our Model: A class defining an Engine.
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

# The controller Class, in this case, a Mediator between the Model and the View.
class Controller(object):
    def __init__(self):
        # The controller needs references to the views.
        self._views = []
        # It can also listen to multiple models, but in this simple case
        # We only have one.
        self._model = None

    def setModel(self, model):
        self._model = model
        # Only the Controller registers itself for notifications
        # from the Model. This is different from Traditional MVC,
        # where the View must do so, and the Controller only if
        # needed.
        model.register(self)

    def addView(self, view):
        # The View gets the Controller reference so that it can
        # act on it in response to GUI events.
        view.setController(self)
        # We add a view to the Controller.
        self._views.append(view)

    def changeRpm(self, rpm):
        # When the GUI events occur, the View pass them to the Controller,
        # either at a high level semantic (like we do here: changeRpm) or
        # at a low level semantic (e.g. a valueChanged method on the
        # Controller). Note however that all the Views must be aware of the
        # Controller interface.
        if self._model:
            # The Controller just passes the value to the Model.
            # This will trigger a notification.
            self._model.setRpm(rpm)

    def notify(self):
        # When the model changes, this method is called.
        # The controller goes through its views, and deliver
        # the information. Note how the two Views handle the value
        # in different ways: the slider handles values from 0 to 10000
        # but the slider from 0 to 10. The conversion is done in the
        # respective Views because this detail is strictly View dependent.
        # The controller would have to treat the views differently if it had
        # to perform this conversion, something that is impractical.
        for view in self._views:
            view.setRpmValue(self._model.rpm())


# One of our Views, specifically, the Dial-like rpm gauge.
class Dial(QtGui.QDial):
    def __init__(self, *args, **kwargs):
        super(Dial, self).__init__(*args, **kwargs)
        self._controller = None
        self.setRange(0,10000)

    def setRpmValue(self, rpm_value):
        self.setValue(rpm_value)

    def setController(self, controller):
        # Sets the controller and connects the GUI event to a callback on its interface.
        # Here we can perform the connection directly. In the next View, we must introduce
        # an additional step.
        self._controller = controller
        self.connect(self, QtCore.SIGNAL("valueChanged(int)"), self._controller.changeRpm)


# The Slider View.
class Slider(QtGui.QSlider):
    def __init__(self, *args, **kwargs):
        super(Slider, self).__init__(*args, **kwargs)
        self._controller = None
        self.connect(self, QtCore.SIGNAL("valueChanged(int)"), self._rpmValueChanged)
        self.setRange(0,10)

    def setRpmValue(self, rpm_value):
        self.setValue(rpm_value/1000)

    def setController(self, controller):
        self._controller = controller

    def _rpmValueChanged(self, value):
        if self._controller:
            self._controller.changeRpm(value*1000)


# Application startup
app = QtGui.QApplication(sys.argv)

container = QtGui.QWidget()
layout = QtGui.QHBoxLayout()
engine = Engine()
dial = Dial(container)
slider = Slider(container)
controller = Controller()
controller.addView(dial)
controller.addView(slider)
controller.setModel(engine)

container.setLayout(layout)
layout.addWidget(dial)
layout.addWidget(slider)


container.show()
app.exec_()

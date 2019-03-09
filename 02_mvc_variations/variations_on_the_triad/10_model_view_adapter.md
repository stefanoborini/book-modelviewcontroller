---
parent: Variations on the triad
---
# Model-View-Adapter (MVA, Mediated MVC, Model-Mediator-View)

### Motivation

Model-View-Adapter is a variation of the Triad where all communication between
Model and View must flow through a Controller, instead of interacting directly
as in a Traditional MVC Triad.  The Controller becomes a communication hub,
accepting change notifications from Model objects and UI events from the View.

This approach might appear excessively strict, but has some advantages: the
communication network is artificially constrained, making it easier to evaluate
and debug. All action happens in the Controller, and the View can be created
from off-the-shelf widgets without any Model-specific variation.

# Design

MVA is an implementation of the Mediator pattern. Controllers are 
generally referred as Adapters or Mediators. The Model and the View 
do not hold references to each other, they do not exchange data nor 
interact directly. 

<p align="center">
    <img src="images/model_view_adapter/ModelViewAdapter.png" width="200">
</p>

The pattern of communication in MVA can be represented with the following
interaction diagram

<p align="center">
    <img src="images/model_view_adapter/MVA_Communication.png" />
</p>

which can be described as

1. The View receives a UI event. It calls an appropriate method on the Controller.
2. The Controller sets the value on the Model.
3. The Model notifies its listeners of the change, among which is the Controller itself. 
   As already pointed out, in a MVC approach this notification would be sent to the View. 
4. The notified Controller fetches information from the Model and updates the View.

With the Controller in full control on the dialog between the two remaining
parties, smart tricks can be performed on the “in transit” data: for example,
the Controller could be responsible for formatting, translating or ordering
the data from the Model.  

### Practical Example 1: With Subclassing of the Views

common in Apple OSX Cocoa Framework. 

We examine a MVA implementation of the Engine example in two steps. In the first step, we will keep subclassing the Views, to present the general concept. In the second step, we will remove the need for subclassing the Views.

The Model is unchanged: it stores rotations per minute information and notifies about changes 

```python
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
```

The two View classes, `Dial` and `Slider`, are now unaware of the Model. Instead,
they know about the Controller, and accept changes to their content through the
`setRpmValue()` method.  A matter of taste can decide the semantic level of this
method. Should it talk “domain language” (i.e. Rpm) or not (i.e. the method
should just be named setValue). In any case, Views behave differently with
respect to the issued value (the Slider needs its value scaled appropriately). 
One could handle this difference in the Controller, but this will be considered 
in the next step.

When the user interacts with the `Dial`, the Controller
`changeRpm()` method is directly invoked, in this case via the Qt Signal/Slot
mechanism 

```python
class Dial(QtGui.QDial):
   def __init__(self, *args, **kwargs):
       super(Dial, self).__init__(*args, **kwargs)
       self._controller = None
       self.setRange(0, 10000)

   def setRpmValue(self, rpm_value):
       self.setValue(rpm_value)

   def setController(self, controller):
       self._controller = controller
       self.connect(self, QtCore.SIGNAL("valueChanged(int)"),
                          self._controller.changeRpm)
```

For the `Slider`, the interface is the same, but the internal implementation is
different. Again, the `setRpmValue` allows the Controller to change the
View contents. In this case however, a proper transformation of the data is
performed to deal with the specifics of the `Slider` behavior, whose range is
from 0 to 10.  Similarly, when the User interact with the `Slider`, the method
`_valueChanged` will be invoked, which in turn will issue a call to the
Controller `changeRpm()` method, after transformation of the parameter

```python
class Slider(QtGui.QSlider):
   def __init__(self, *args, **kwargs):
       super(Slider, self).__init__(*args, **kwargs)
       self._controller = None
       self.connect(self, QtCore.SIGNAL("valueChanged(int)"),
                          self._valueChanged)
       self.setRange(0,10)

   def setRpmValue(self, rpm_value):
       self.setValue(rpm_value/1000)

   def setController(self, controller):
       self._controller = controller

   def _valueChanged(self, value):
       if self._controller:
           self._controller.changeRpm(value*1000)
```

The Controller class handles the Model and the two Views accordingly. It
registers for notifications on the Model, and it receives notification from the
Views on its `changeRpm()` method, where it modifies the contents of the Model.
When the Model communicates a change, it pushes the new value to the Views

```python
class Controller(object):
   def __init__(self):
       self._views = []
       self._model = None

   def setModel(self, model):
       self._model = model
       model.register(self)

   def addView(self, view):
       view.setController(self)
       self._views.append(view)

   def changeRpm(self, rpm):
       if self._model:
           self._model.setRpm(rpm)

   def notify(self):
       for view in self._views:
           view.setRpmValue(self._model.rpm())
```

### Practical Example 2: With generic Views

In the previous example, removing the dependency of the Views on the Model did not allow us to use generic Views. In this example we will move the value translation logic
from the Views to the Controller, thus removing the need for subclassing the Views, an important advantage of MVA.

```python
class Controller(object):
   def __init__(self, model, slider, dial):
       self._slider = slider
       self._dial = dial
       self.connect(self._slider, QtCore.SIGNAL("valueChanged(int)"),
                          self._sliderChanged)
       self.connect(self._dial, QtCore.SIGNAL("valueChanged(int)"),
                          self._dialChanged)
       self._model = model
       model.register(self)

   def changeRpm(self, rpm):
       if self._model:
           self._model.setRpm(rpm)

   def notify(self):
       for view in self._views:
           view.setRpmValue(self._model.rpm())
```




### Practical Example 3: With forwarding of Model events

If the Model emits qualified events, the Controller could simply forward them
to the View.


Model-GUI-Mediator
------------------

**Addressed Need:**

One problem with Model-View-Adapter is that it assumes the Views are derived
classes, each implementing specific behavior. In the previous example, each
View performed a specific transformation to the data before displaying: the
Dial left it as is, while the Slider divided it by 1000. In the
Model-GUI-Mediator, the desire is not to reimplement the toolkit's widgets,
because it generally leads to proliferation of View classes. Instead, widgets
are used as they are, off-the-shelf from the toolkit. The obvious consequence
is that logic that is pertinent to the conversion of data for visualization
must go somewhere else. The Controller seems the obvious choice, however
keeping the same design as in MVA would be cumbersome: the single Controller
would have to differentiate the Views, and submit properly transformed data to
each View.  A better solution is to have different Controllers, one per each
View, doing the relevant transformation.  The code would therefore be like the
following: The View being an off-the-shelf component means it does not know
anything about the Controller. All the signal setup is done by the individual
Controllers. Also, off-the-shelf classes are not implementing the Observer
pattern

.. code-block:: python

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
           self._view.connect(self._view, 
                              QtCore.SIGNAL("valueChanged(int)"),
                              self.changeRpm)

       def changeRpm(self, rpm):
           if self._model:
               self._model.setRpm(rpm)

       def notify(self):
           if self._view:
               self._view.setValue(self._model.rpm())


And for the Slider it would be 

.. code-block:: python

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
           self._view.connect(self._view, 
                              QtCore.SIGNAL("valueChanged(int)"),
                              self.changeRpm)

       def changeRpm(self, rpm):
           if self._model:
               self._model.setRpm(rpm*1000)

       def notify(self):
           self._view.setValue(self._model.rpm()/1000)

The setup now can simply make use of off-the-shelf QDial and QSlider instances

.. code-block:: python

   dial = QtGui.QDial(container)
   dial_controller = DialController()
   dial_controller.setView(dial)
   dial_controller.setModel(engine)

   slider = QtGui.QSlider(container)
   slider_controller = SliderController()
   slider_controller.setView(slider)
   slider_controller.setModel(engine)

The Model-GUI-Mediator approach basically has the Controller adapt the
off-the-shelf widget to be aware of the Model. This requires no subclassing. In
a sense, Model-GUI-Mediator is similar to Document-View, but it reorganizes
competences in a different way and splits the View into off-the-shelf
functionality and application-contextual functionality.


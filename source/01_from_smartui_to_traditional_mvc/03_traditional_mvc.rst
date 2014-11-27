Traditional MVC
---------------

**Additional need: separate visualization operations from modification operations.**

With the Document-View design we successfully extracted state from an initial
Smart-UI design. The next objective is to extract the code that converts the
primary event (in this case, a mouse click on the button) into the execution of
the logic that modifies the state (addition of one to the value). The final
result of this refactoring will be a **Traditional MVC** design.  

In Traditional MVC, the Document is called **Model**, and its role and structure is
unchanged: it stores state and delivers change notifications. The visual part
is divided into two classes, the **Controller** and the **View**. Once instantiated and
connected, Model, View, and Controller form a so-called **MVC triad**.

.. image:: ../_static/images/TraditionalMVC/mvc_triad.png
   :align: center

FIXME Put a more appropriate image, expressing the strong and weak association between entities.


The Controller's role is to transform primary events delivered by the View into
operations on the Model. Depending on the specifics of the application, a Controller may or may not need
a reference to the View, but it certainly needs the Model to apply changes on ::

   class Controller(object):
       def __init__(self, model, view):
           self._model = model
           self._view = view

The method ``addOne`` performs the specific task of transforming a primary event
into a Model operation, adding one to the current value.  Obviously, the
Controller does so through the Model interface. This operation will trigger a
Model notification to its listeners ::

    class Controller(object):
        # ...
        def addOne(self):
            self._model.setValue(self._model.value()+1)

At initialization, the View instantiates its associated Controller, passing
itself and the Model as parameters. As before, the View registers itself on the
Model via the ``register`` method ::

    class View(QtGui.QPushButton):
        def __init__(self, model):
            super(View, self).__init__()
            self._model = model
            self._controller = Controller(self._model, self)
            self._model.register(self)

The View now depends on the Controller to modify the Model: only strictly
GUI-related handling is done by the View. Conversion from GUI events to
application business logic is delegated to the Controller in
``mouseReleaseEvent`` ::

    class View(QtGui.QPushButton):
        # ...
        def mouseReleaseEvent(self, event):
            super(View, self).mouseReleaseEvent(event)  
            self._controller.addOne()  

        def notify(self):
            self.setText(unicode(self._model.value()))   

Clicking on the View button will result in a call to ``Controller.addOne``, in
turn triggering a call to ``notify`` that updates the text label. The activity
diagram shows the dance of calls presented above. Note how the Model-View
synchronization does not involve the Controller

.. image:: ../_static/images/TraditionalMVC/activity_diagram.png
   :align: center

To initialize the MVC triad, the client code needs to create the Model and
View, and let them be aware of each other by passing the Model to the View. ::

   app = QtGui.QApplication(sys.argv)

   model = Model()
   view = View(model)
   view.show()

   app.exec_()

The activity diagram shows the setup code given above

.. image:: ../_static/images/TraditionalMVC/activity_diagram_setup.png
   :align: center

This schema assumes that the controller is initialized by the View. This is generally
desirable, given that View and Controller are so dependent and tailored to each
other that passing the Controller from outside is not profitable. 


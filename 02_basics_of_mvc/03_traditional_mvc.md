---
parent: Basics of MVC
nav_order: 3
permalink: /basics-of-mvc/traditional-mvc/
---
# Traditional MVC

With the Document-View design we successfully extracted state from an initial
Smart-UI design. The next objective is to extract the code that converts the
primary event (in this case, a mouse click on the button) into the execution of
the logic that modifies the state (addition of one to the value). The final
result of this refactoring will be a **Traditional MVC** design[^1].

In Traditional MVC, the Document is called **Model**, and its role 
and structure is unchanged: it stores state and delivers change
notifications. The View part is divided into two classes, the
**Controller** and the **View**. Once instantiated and connected, 
Model, View, and Controller form a so-called **MVC triad**.

<p align="center">
  <img src="images/mvc_triad.png" />
</p>

The Controller's role is to transform primary events delivered by the View into
operations on the Model. Depending on the specifics of the application, a Controller may or may not need
a reference to the View, but it certainly needs the Model to apply changes on

```python
class Controller(object):
   def __init__(self, model, view):
       self._model = model
       self._view = view
```

The method ``addOne`` performs the specific task of transforming a primary event
into a Model operation, adding one to the current value.  Obviously, the
Controller does so through the Model interface. This operation will trigger a
Model notification to its listeners 

```python
class Controller(object):
    # ...
    def addOne(self):
        self._model.setValue(self._model.value()+1)
```

At initialization, the View instantiates its associated Controller, passing
itself and the Model as parameters. As before, the View registers itself on the
Model via the ``register`` method 

```python
class View(QtGui.QPushButton):
    def __init__(self, model):
        super(View, self).__init__()
        self._model = model
        self._controller = Controller(self._model, self)
        self._model.register(self)
```

The View now depends on the Controller to modify the Model: only strictly
GUI-related handling is done by the View. Conversion from GUI events to
application business logic is delegated to the Controller in
``mouseReleaseEvent`` 

```python
class View(QtGui.QPushButton):
    # ...
    def mouseReleaseEvent(self, event):
        super(View, self).mouseReleaseEvent(event)  
        self._controller.addOne()  

    def notify(self):
        self.setText(unicode(self._model.value()))   
```

Clicking on the View button will result in a call to ``Controller.addOne``, in
turn triggering a call to ``notify`` that updates the text label. The activity
diagram shows the dance of calls presented above. Note how the Model-View
synchronization does not involve the Controller

<p align="center">
  <img src="images/activity_diagram.png">
</p>

To initialize the MVC triad, the client code needs to create the Model and
View, and let them be aware of each other by passing the Model to the View. 

```python
app = QtGui.QApplication(sys.argv)

model = Model()
view = View(model)
view.show()

app.exec_()
```

The activity diagram shows the setup code given above

<p align="center">
  <img src="images/activity_diagram_setup.png">
</p>

This schema assumes that the controller is initialized by the View. This is generally
desirable, given that View and Controller are so dependent and tailored to each
other that passing the Controller from outside is not profitable. 

FIXME
The direct connection between View and Controller is needed for:
1) the View initializes the controller with an instance of itself at
creation
2) the currently active controller can be found by traversing the view hierarchy

FIXME: Strictly speaking, the controller does not need to know about the View:
the controller receives events (from the user) and modifies the model, and the model
syncs against the view. In practice. the user interacts with a view object, and the associated
controller handles that operation.

[^1] The more knowledgeable reader may recognize that this MVC model 
is not the original MVC as intended in its first implementation. 
We will go into detail of the differences in later chapters. 
What is presented here is the modern reinterpretation of the 
original MVC, and the one most likely to be intended when talking 
about "MVC". To clarify the overloaded nomenclature, I chose to 
refer to the original '70s design as  "Reenskaug MVC", and its 
modern reinterpretation here presented as "Traditional MVC".

From Smart-UI to Traditional MVC
================================

Smart-UI: A single class with many responsibilities
---------------------------------------------------

We start this exploration of MVC with the most trivial and simplistic
application: a click counter. This application shows a button with a number.
The number is increased every time the button is clicked. 
    
.. image:: _static/images/SmartUI.png
   :align: center

We can implement this application as follows::

    import sys
    from PyQt4 import QtCore, QtGui

    class Counter(QtGui.QPushButton):
        def __init__(self, *args, **kwargs):
            super(Counter, self).__init__(*args, **kwargs)
            self._value = 0
            self._update()

        def mouseReleaseEvent(self, event):
            super(Counter, self).mouseReleaseEvent(event)
            self._value += 1
            self._update()

        def _update(self):
            self.setText(unicode(self._value))

    app = QtGui.QApplication(sys.argv)
    counter = Counter()
    counter.show()
    app.exec_()

The application's main and only visual component, Counter, is derived from a
single GUI class, a Qt ``QPushButton``. The Counter class holds multiple
responsibilities: 

    1. Stores the current click count value in the member variable ``self._value``. 

    2. Handles the logic that modifies ``self._value``. Every time the button is
       clicked, Qt invokes ``mouseReleaseEvent`` automatically. In this method 
       the click counter is incremented.
    3. Synchronizes the aspect of the button with the current ``self._value``, 
       by invoking ``setText``.

Combining these three responsibilities into a single class gives us the so
called **Smart-UI** design. While appealing for its simplicity and compactness,
this design does not scale well to larger applications, where state, user
events and graphic layout are more complex and intertwined, and need to change
often. In particular, we can observe the following issues with the current
design, as we imagine to scale it up:

   - Access and modification of the current value from outside is cumbersome, being
     contained into an all-encompassing visual object: external objects that want to
     modify the current counter need to make sure that the represented value is
     synchronized.

   - It is difficult for multiple visual objects to visualize the same information,
     maybe with two different visual aspects (*e.g.* both as a counter and as a
     progress bar)

   - The logic dealing with visual aspect (i.e. handling and layouting widgets,
     updating the label on the button), interaction aspect (handling the user
     initiated mouse click to perform the increment operation) and business aspect
     (incrementing the counter) are of different nature, and would be better kept
     separated. This would ease testability, simplify code understanding and
     interaction.

Document-View: dividing state from GUI
--------------------------------------

**Additional Need**: Represent the same information in two visual forms at the same time.

To solve the shortcomings of Smart-UI, we take advantage of the intrinsic
division into visual, interaction and business role expressed by a GUI
application. In Smart-UI, these three roles happen to be assigned to the same
class, but we can reorganize our code so that they are kept separated. The
resulting design is a two-class system known in literature as **Document-View** or
**Model-Delegate**.  

The first step is to partition out the data, represented by the ``self._value``
variable, into a separate class ``Document``. For our system to continue to work,
the visual part **View** must now be informed of changes to this data. The Document
will therefore not only hold ``self._value``, but also provide an interface to
query and modify this data and a strategy to notify other objects when changes
occur. This is expressed in the following implementation code ::

    class CounterDocument(object): 
        def __init__(self): 
            self._value = 0 
            self._listeners = set() 

In addition to the value, the ``self._listeners`` member variable holds references
to external objects interested in being notified about changes. We use a python
set instead of a list to prevent accidental registration of the same object
twice. Interested objects can register and unregister through the following
methods :: 

    def register(self, listener): 
        self._listeners.add(listener) 
        listener.notify() 

    def unregister(self, listener): 
        self._listeners.remove(listener) 

Finally, we provide a setter/getter method pair [#]_ for ``self._value``: 
the getter method is trivial, and simply returns the value ::

        def value(self): 
            return self._value 

while the setter modifies the internal variable and notifies the registered
listeners when the value changes. This is done by calling the listeners'
``notify`` method, as you can see in ``self._notifyListeners`` ::

        def setValue(self, value): 
            if value != self._value: 
                self._value = value 
                self._notifyListeners() 

        def _notifyListeners(self): 
            for l in self._listeners: 
                l.notify()

The method ``notify`` is therefore the interface that a registered listener
must provide in order to receive notifications about the mutated state of the
Document object. Our View need to implement this method. 

The View class will be responsible for rendering the information contained in
an instance of ``CounterDocument``. This instance is passed at initialization,
and after a few formalities, the View register itself for notifications ::

    class CounterView(QtGui.QPushButton):
        def __init__(self, document):
            super(CounterView, self).__init__()
            self._document = document
            self._document.register(self)

When this happens, the Document adds the View as a listener. A notification is
immediately delivered to the newly added listener so that it can update
itself. [#]_ The ``notify`` method on the View is then called, which will query
the current value from the Document, and update the text on the button ::

        def notify(self):
            self.setText(unicode(self._document.value()))

Note how this method inquires the Document through its interface (calling
``CounterDocument.value``). The View must therefore have detailed knowledge of its
associated Model's interface and must deal with the semantic level it presents.
Through this knowledge, the View extracts data from the Model, and converts
“Model language” into “View language” to present the data into the visual
widgets it is composed of.  

Handling of the click event from the User is performed in
``mouseReleaseEvent``, as in Smart-UI. This time however, the action will
involve the Document, again through its interface ::

        def mouseReleaseEvent(self, event):
            super(CounterView, self).mouseReleaseEvent(event)
            self._document.setValue(self._document.value()+1)

the ``setValue`` call will then issue a change notification that will update the
button text via ``notify``.

With this new design, we open the possibility for different GUI objects to stay
synchronized against the Document state, something that would not have been
possible with Smart-UI. We can now provide different representation modes for
the same information, or modify it through different sources, either visual or
non-visual. We can for example add a Progress Bar ::

    class ProgressBarView(QtGui.QProgressBar):
        def __init__(self, document):
            super(ProgressBarView, self).__init__()
            self._document = document
            self._document.register(self)
            self.setRange(0,100)

        def notify(self):
            self.setValue(self._document.value())

and register it on the same Document instance at initialization ::

    app = QtGui.QApplication(sys.argv)

    document = CounterDocument()
    counter = CounterView(document)
    progress = ProgressBarView(document)

    counter.show()
    progress.show()

    app.exec_()

When the button is clicked, both its label and the progress bar are kept
updated with the current value in the Document.

The Document-View design achieves separation of the state from its graphical
representation, allowing them to change independently. The Document has become
a fully non-GUI entity that can act and be tested independently. Any registered
View always keeps itself up-to-date against the Document contents through the
notification system, and carry full responsibility for graphical rendering of
the Document information and the handling of user interaction.

.. [#] Python properties can be used for the same goal. However, python properties are
   harder to connect to the signal/slots mechanism in PyQt. 

.. [#] When registration of the View on the Document is done in the View's
   initializer, as we are doing here, it should be done only when the
   initialization is completed, so that notify can be called on a fully
   initialized object. An alternative strategy is to delay this setup and perform
   it through a View.setDocument method.


.. note:: **Notification system in strongly typed languages**
   
   A possible implementation of the notification system in strongly typed
   languages uses an interface class ListenerInterface with one abstract method
   notify(). For example, in C++ we would write the following code

   .. code-block:: cpp

      class ListenerIface 
      {
      public:
          virtual void notify() = 0;
      };

      Concrete listeners will implement this interface
      class View : public ListenerIface
      {
      public:
          void notify();
      };

   The Model will accept and handle pointers to the Listener interface, thus
   not requiring a dependency toward specific Views or Controllers

   .. code-block:: cpp

      class Model 
      {
      public:
          void register(ListenerIface *listener) 
          {
              listeners.push_back(listener);
          }

      private:
          void notifyListeners() 
          {
              std::vector<ListenerIface *>::iterator it;
              for (it = listeners.begin(); it != listeners.end(); ++it) {
                      (*it)->notify();
          }

          std::vector<ListenerIface *> listeners;
      };

   A similar approach can be used in Java.


.. silence ** in vim


Traditional MVC
---------------

**Additional need**: separate visualization operations from modification operations

With the Document-View design we successfully extracted state from an initial
Smart-UI design. The next objective is to extract the code that converts the
primary event (in this case, a mouse click on the button) into the execution of
the logic that modifies the state (addition of one to the value). The final
result of this refactoring will be a **Traditional MVC** design.  

In Traditional MVC, the Document is called **Model**, and its role and structure is
unchanged: it stores state and delivers change notifications. The visual part
is divided into two classes, the **Controller** and the **View**. Once instantiated and
connected, Model, View, and Controller form a so-called **MVC triad**.

.. image:: _static/images/TraditionalMVC/mvc_triad.png
   :align: center

The Controller's role is to transform primary events delivered by the View into
operations on the Model. Depending on the specifics of the application, a
Controller may or may not need a reference to the View, but it certainly needs
the Model to apply changes on ::

   class Controller(object):
       def __init__(self, model, view):
           self._model = model
           self._view = view

The method ``addOne`` performs the specific task of transforming a primary event
into a Model operation, adding one to the current value.  Obviously, the
Controller does so through the Model interface. This operation will trigger a
Model notification to its listeners ::

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

    def mouseReleaseEvent(self, event):
        super(View, self).mouseReleaseEvent(event)  
        self._controller.addOne()  

    def notify(self):
        self.setText(unicode(self._model.value()))   

Clicking on the View button will result in a call to ``Controller.addOne``, in
turn triggering a call to ``notify`` that updates the text label. The activity
diagram in Fig. 2 shows the dance of calls presented above. Note how the
Model-View synchronization does not involve the Controller

.. image:: _static/images/TraditionalMVC/activity_diagram.png
   :align: center

To initialize the MVC triad, the client code needs to create the Model and
View, and let them be aware of each other by passing the Model to the View. ::

   app = QtGui.QApplication(sys.argv)

   model = Model()
   view = View(model)
   view.show()

   app.exec_()

The activity diagram in Figure 3 shows the setup code given above

.. image:: _static/images/TraditionalMVC/activity_diagram_setup.png
   :align: center

An in-depth analysis of Traditional MVC roles and components
------------------------------------------------------------

In the previous sections we performed a progressive refactoring from Smart-UI
to Document-View, then to Traditional MVC, driven by the need for additional
flexibility, separation of concerns and clarification of the different roles.
To summarize the scope of each role in Traditional MVC:

   - **Model**: holds the application's state and core functionality.
   - **View**: visually renders the Model to the User.
   - **Controller**: mediates User actions on the GUI to drive modifications on the Model.

Except for the most trivial applications, multiple classes can be active in the
same role and are said to belong to a specific **layer** (i.e. Model layer, View
layer and Controller layer). Objects from these layers are composed into MVC
Triads that give rise to the final application's behavior and aspect.  This
design is blessed with technical advantages: 

   - The clear separation of concerns between data storage, data handling, data
     visualization, and user interaction opens the possibility to be flexible
     in changing their implementation (for example, the layout of the graphical
     interface).

   - The communication among objects is restricted on purpose and characterized
     by its triad interaction pattern, reducing complexity and side effects.

   - Applications that need to visualize the same data in different ways, or
     modify them from different sources (for example, a data table and a plot)
     can do so while keeping the information centralized and synchronized.

   - Separation of concerns leads to easier testability and thus higher
     reliability: each component can be tested independently from the others,
     with their dependencies replaced by mock objects with predictable behavior.

   - Frameworks and GUI toolkits already provide MVC solutions as part of their
     design: you just have to “fill the blanks” to get a working application. 

Additionally, MVC accelerates development, improves readability and communication of intent: 

   - Different teams with different skills can work in parallel on separate
     parts of the application: frontend developers and GUI designers can work
     on the visual aspect, while backend developers and storage scaling specialists
     can work on low-level data representation. 

   - By defining clear interfaces on the protagonists' classes, the code
     documents itself both through the API and their role within the MVC design

   - MVC provides a common vocabulary to talk about roles and responsibilities
     in design.
 
The Model
~~~~~~~~~

Entities taking the Model role are responsible for holding the running state
and business functionality of the application, either as a whole or as the part
that is relevant to that specific MVC Triad, as either data (stored values) or
activity (routines computing relevant data). They define the protagonists of
the application's domain, their mechanism of operation and cooperation. Model
objects can represent, for example, 

   - An interface to a database, filesystem, or low level driver 
   - Access to a computational backend
   - Proxies for a remote service
   - A representation of business entities such as weather forecast in a
     specific area, people's details in a phonebook, tracks information in a
     music CD, student grades
   - In some designs, graphical state of the GUI, such as selected items, or
     the X-axis scale of a plot. 

When implemented, a Model can go from a dictionary-like of key/value pairs to a
complex network of objects with well defined interfaces. Regardless of the
implementation, Models in Traditional MVC must provide the following three
services: 

**Querying**: to inquire about their current state, either represented by
high-level domain objects (Object Oriented approach), or through an IO
layer of routines providing access to the data (Data Oriented approach). In the
Object Oriented approach, the Model objects generally represents an
identifiable part of the domain of your application, and provide access to data
through a well-defined object-oriented interface. The Model can also perform
computation, generally of information derived or associated to the main data it
represents. In the Data Oriented approach, the routines “speak the domain
language” and have high-level semantics to access the data, generally from a
data storage (e.g. disk).

**Altering**: to modify the current state. The Model interface provides set
methods or routines to modify its state. The Model performs consistency
checks about the data it handles, enforcing fundamental integrity: for example,
it can raise an exception or ignore the passed data if a method
setCurrentTemperature is called passing a string instead of a float, or a
method setLength is called with a negative value. 

**Notifying**: to inform interested parties that a change has occurred in its
state. The Model allows interested objects to register themselves for
notifications. When a change occurs, these objects will be notified of this
fact and can act accordingly, normally by synchronizing themselves against the
Model's new contents. 

Model objects should provide core application functionality through a clear and
self-documented interface, exposing what can be done with the program's state.
To operate, they can depend only on other Model objects or other components of
the application that don't involve presentation, like an IO layer. The
relationship among Model objects is that of a **strong dependency**.  

On the other hand, a Model should not contain nor be dependent for its
functionality on any graphical entity, nor contain formatting/visual logic for
presentation (*e.g.* logic to make a negative value represented in red, or logic
to present the date in US vs. ISO representation). Model objects should be
completely unaware of how user interaction is handled by the application they
live in, and should have a **weak dependency** toward its listeners via the
notification generic interface. 

For data modification, all the Model does is to process incoming requests in
the form of method calls.  Normally these requests are performed by
Controllers, but a Model can also change due to requests from other subsystems
(for example, a network layer), from another Model component or because it is
monitoring a backend (e.g. a database, or a filesystem) and the monitored
entity changes. The only entities never allowed to issue a change request to
the Model are the Views.  

The Model should enforce integrity of the data, but it does not necessarily
enforce validity: data might be correct (for example, integers for min/max
values) but overall invalid for computation (for example, if min > max). While
integrity should be enforced, storing invalid data can be acceptable: depending
on the application, invalid data may be marked as such in the Model by the part
of the code that detects the invalidity, so that the View can represent it (for
example, with a red font); An invalid state might be needed as a stepstone to
reach a valid state at the end of a set of changes done by the User via the UI.

With the above guidelines and restrictions in place, the resulting
implementation is robust, flexible and testable: Views and Controllers are the
components that change the most as the application evolves, and a Model that is
agnostic to these changes is easier to code and maintain. The Model can be
tested independently from the rest of the application, and it opens itself to
scripting, allowing the User to change the Model programmatically instead of
through the GUI. 

The View
~~~~~~~~
We introduced the View as the component of our application whose role is to
render Model contents to the User. A View listens for Model notifications and
responds by fetching and rendering the new state. This results in a strong
dependency toward the Model: Views must access Model data, something that
requires full dependency toward the Model's interface and existence. 

Views are responsible for "purely GUI" intelligence, like handling behavior on
resizing, repainting, data displaying and visual formatting. They are also in
charge of handling primary events such as mouse clicks and keyboard key
presses, but should not perform any modifying action on the Model as a
consequence to these events. Instead, they should delegate this task to
Controllers. They should also not perform any operation that is competence of
the Model, nor store Model data, except for caching to improve rendering
performance. Cached data are never authoritative, and should never be pushed
back into the Model, or handed out to other objects. 

A View is generally composed out of **Widgets**, reusable visual building
blocks provided by a Widget toolkit library. Examples of widgets are buttons,
checkboxes, and menus. Complex interfaces are assembled from a collection of
Widgets, hierarchically contained in dialogs, windows and other visual
containers. This intrinsic hierarchic nesting must be factored in when we want
to go from the basic MVC given in the previous section to a real-world MVC. The
hierarchy is bidirectional, meaning that containers hold references to the
contained widgets, and vice versa. Widget state is normally modified from
client code via method calls, having no intelligence for receiving
notifications from the Model. A View adds Model observing capabilities and
rendering logic to a widget or groups of widgets, either through inheritance or
composition.

MVC is not only limited to GUI representations, and Views are not necessarily
graphical objects. In fact, anything that can report information to the User in
some form can be classified as a View. For example, a musical notation Model
can be observed by two Views: one that shows the musical notation on screen and
another that plays it on the speakers. 

The Controller
~~~~~~~~~~~~~~

The last of the components of MVC, the Controller, has the heavy duty task to
make things happen by gathering, validating, and processing User events to
modify the state of the application. 

Controllers are associated to Views in a strong one-to-one mutual dependency,
and can be described as the “business logic” of the View. When the View
receives a primary event, it forwards execution to an appropriate Controller
method, where appropriate logic modifies the state of the application.
Generally, the change is applied to the Model, but depending on the problem the
Controller can also directly modify the View, in particular when it changes
visual state that is purely pertinent to the View and is not represented in the
Model. Examples of these cases can be enabling/disabling some widget,
scaling/zooming of a plot area, reordering of menu entries and so on. 

A Controller generally hosts a reference to its View and the Models it
modifies, and depends strongly on their interfaces and presentation semantics,
at least to a degree. It may act on Models that are not the ones observed by
the associated View. Like Views, a Controller can be a listener for Model
notifications, when the Model state influences how the Controller interprets
the User events. 


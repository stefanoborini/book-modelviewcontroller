---
parent: 2. Basics of MVC
nav_order: 2
---
# 2.2 Document-View: dividing state from GUI

To solve the shortcomings of Smart UI, we take advantage of the intrinsic
division into visual rendering, interaction and business logic expressed by a GUI
application. In Smart UI, these three roles happen to be assigned to the same
class, but we can reorganize our code so that the business logic part is kept
separated. The resulting design is a two-class system known in literature as 
**Document View** or **Model Delegate**.

The **Document** class is responsible for handling the business logic.
It has no part in dealing with graphical rendering, nor with GUI events. It
simply stores application relevant state, and provides an interface to obtain this
state or change it according to the rules of the application. Additionally, it
provides a mechanism to inform interested objects of changes. 

The **View** class instead handles user events, renders itself visually,
performs operations on the Document and keeps its visual aspect synchronized
against the Document's state when it changes. 

The Document-View design achieves separation of the state from its graphical
representation, allowing them to change independently. The Document has become
a fully non-GUI entity that can act and be tested independently. Any registered
View always keeps itself up-to-date against the Document contents through the
notification system, and carry full responsibility for graphical rendering of
the Document information and the handling of user interaction.

This design removes some of the concerns expressed for Smart UI. Testing of the
state and business logic becomes easier: the Document object can be modified or
accessed programmatically by issuing calls to its methods. This object is now
independent and can work and manipulated with different Views, if desired. An
additional price in complexity is introduced in having to keep the View (or Views) notified of changes to the Document.

## Implementation example

We can implement this design to our Click counter application through progressive refactorings. The first step is to partition out the data, represented by the ``self._value`` variable, into the Document class. For our system to continue to work, the visual part View must now be informed of changes to this data. The Document will therefore not only hold ``self._value``, but also provide an interface to query and modify this data and a strategy to notify other objects when changes occur. This is expressed in the following implementation code  

```python
class CounterDocument(object): 
   def __init__(self): 
       self._value = 0 
       self._listeners = set() 
```

In addition to the value, the ``self._listeners`` member variable holds references to Views interested in being notified about changes. We use a python set instead of a list to prevent accidental registration of the same object twice. Interested objects can register and unregister through the following methods 

```python
class CounterDocument(object): 
  # ...
  def register(self, listener): 
      self._listeners.add(listener) 
      listener.notify() 

  def unregister(self, listener): 
      self._listeners.remove(listener)  
```

We then provide a getter method [^1] for ``self._value``: 

```python
class CounterDocument(object): 
   # ...
   def value(self): 
       return self._value 
```

We also provide a setter to directly set a specific value. Note in particular how the method notifies the registered listeners when the value changes. This is
done by calling the listeners' ``notify`` method, as you can see in
``self._notifyListeners``

```python

class CounterDocument(object): 
   # ...
   def setValue(self, value): 
       if value != self._value: 
           self._value = value 
           self._notifyListeners() 

   def _notifyListeners(self): 
       for l in self._listeners: 
           l.notify()
```

The method ``notify`` is therefore the interface that a registered listener
must provide in order to receive notifications about the mutated state of the
Document object. Our View need to implement this method. 

Finally, we also provide a method that increments the value according to the
expected logic

```python
class CounterDocument(object): 
   # ...
   def incrementValue(self): 
       self._value += 1
       self._notifyListeners() 
```

The View class will be responsible for rendering the information contained in
an instance of ``CounterDocument``. This instance is passed at initialization,
and after a few formalities, the View register itself for notifications

```python
class CounterView(QtGui.QPushButton):
   def __init__(self, document):
       super(CounterView, self).__init__()
       self._document = document
       self._document.register(self)
```

When this happens, the Document adds the View as a listener. A notification is
immediately delivered to the newly added listener so that it can update
itself. The ``notify`` method on the View is then called, which will query the current value from the Document, and update the text on the button

```
class CounterView(QtGui.QPushButton):
   # ...
   def notify(self):
       self.setText(unicode(self._document.value()))
```

Note how this method inquires the Document through its interface (calling
``CounterDocument.value``). The View must therefore have detailed knowledge of its associated Model's interface and must deal with the semantic level it presents. Through this knowledge, the View extracts data from the Model, and converts “Model language” into “View language” to present the data into the visual widgets it is composed of.  

Handling of the click event from the User is performed in ``mouseReleaseEvent``, as in Smart-UI. This time however, the action will involve the Document, again through its interface 

```python
   class CounterView(QtGui.QPushButton):
       # ...
       def mouseReleaseEvent(self, event):
           super(CounterView, self).mouseReleaseEvent(event)
           self._document.incrementValue()
```

the ``setValue`` call will then issue a change notification that will update the
button text via ``notify``.

We can now provide multiple Views with different representation modes for the
same information, or modify it through different sources, either visual or
non-visual. We can for example add a Progress Bar

```python
class ProgressBarView(QtGui.QProgressBar):
   def __init__(self, document):
       super(ProgressBarView, self).__init__()
       self._document = document
       self._document.register(self)
       self.setRange(0,100)

   def notify(self):
       self.setValue(self._document.value())
```

and register it on the same Document instance at initialization 

```python
app = QtGui.QApplication(sys.argv)

document = CounterDocument()
counter = CounterView(document)
progress = ProgressBarView(document)

counter.show()
progress.show()

app.exec_()
```

When the button is clicked, both its label and the progress bar are kept
updated with the current value in the Document.

[^1] Python properties can be used for the same goal. However, python properties are harder to connect to the signal/slots mechanism in PyQt. 

[^2] When registration of the View on the Document is done in the View's
initializer, as we are doing here, it should be done only when the
initialization is completed, so that notify can be called on a fully
initialized object. An alternative strategy is to delay this setup and perform it through a `View.setDocument` method.

-----

**Notification system in strongly typed languages**

A possible implementation of the notification system in strongly typed
languages uses an interface class `ListenerInterface` with one abstract method
`notify()`. For example, in C++ we could write the following code

```cpp
class ListenerIface 
{
public:
    virtual void notify() = 0;
};
```

Concrete listeners will implement this interface

```cpp

class View : public ListenerIface
{
public:
    void notify();
};
```

The Model will accept and handle pointers to the Listener interface, thus
not requiring a dependency toward specific Views or Controllers

```cpp

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
```

A similar approach can be used in Java.

-----------

# Visual Proxy

### Motivation

Visual Proxy is an approach first presented by Allen Holub in 1999. It
it is wildly different from the previous approaches, but definitely contains
interesting ideas. Holub argues the following:

- It is very rare for the same Model to be represented at the same 
time in two different ways. 
- Model representation is not about the Model object per-se, but
for some specific attributes of that object. These attributes 
can be presented with a well defined UI widget, regardless of 
where they will appear in the View. For example, 
``Person.name`` is invariably represented as a string, 
and its View presentation is an editable textfield widget throughout
the application.
- All Model designs generally assume a get/set approach to
Model state modification. From a strict Object Oriented interpretation,
getter/setters is a *faux pas* and should be avoided, as they are
just access to private state in disguise. 
- Essential separation between Model and View is clumsy to
achieve in MVC, which does not scale well at the application level.
- An Object Oriented system should focus on objects issuing behavior
requests to one another, with the data staying put. The previous designs
instead focus on data transfer from the view to the model, and *vice-versa*.

Out of these considerations, the proposed alternative is to let Models 
create their own Views, according to the data they hold. For example, 
a Model containing a string, a date and an integer range return 
a View containing a LineEdit, a Calendar and a Spinbox constrained
to the the appropriate range.

This approach, while appealing in its cleverness, is not without 
shortcomings. Responsibilities that are traditionally handled by 
the View layer are now handled, directly or indirectly, by the Model:

- the Model layer has a dependency on the GUI toolkit.
This may have deep implications for testability and reuse. 
- If the Visual Proxy contains static parts (such as a "Name" label
followed by the line editor to input the name) the Model objects 
have to handle localization of the "Name" string in other languages.
- Logical dependencies between visual components (*e.g.* when this 
value is 1, enable that checkbox) must also be moved to the 
Model layer.

Note that this approach is different from UI Retrieving Model. 
The latter considers the user as a source of data, and generates
a short-lived UI for that specific retrieval. Visual Proxy, on the 
other hand, is a full fledged foundation of all Model objects 
to provide their own View as implicitly described by their data.

### Design

Model objects act as factories for the UI of their own attributes

<p align="center">
    <img src="images/visual_proxy/visual_proxy.png" />
</p>

The resulting message flow is simplified: all the data synchronization happens 
between the Visual Proxy and its backend attribute. The Client code
is not concerned with this transaction. It just coordinates
creation and presentation of Visual Proxy object to the User.

# Practical Example 

The following practical example represents a boilerplate 
implementation of the design. Two methods are provided 
to generate a Visual Proxy: `visualProxyAttribute` returns
the Proxy for a specific attribute of the Person Model class;
`visualProxy` returns instead the full UI representation of the 
Model properties.

For simplicity of presentation, this example only performs 
synchronization in one direction, from the View to the Model.
Changes in the Model are not updating the View.

```python
class Person(object):
    def __init__(self, name="", surname="", age=0):
        self._name = name
        self._surname = surname
        self._age = age

    def visualProxy(self, read_only=False):
        view = QWidget()
        layout = QGridLayout()
        for row, attr in enumerate(["name", "surname", "age"]):
            layout.addWidget(QLabel(attr), row, 0)
            layout.addWidget(self.visualProxyAttribute(attr, read_only), row, 1)
        view.setLayout(layout)
        return view
        
    def visualProxyAttribute(self, attribute, read_only=False):
        create_map = {
            "name": self._createNameView,
            "surname": self._createSurnameView,
            "age": self._createAgeView,
        }

        return create_map[attribute](read_only)

    def _updateName(self, name):
        self._name = name

    def _updateSurname(self, surname):
        self._surname = surname

    def _updateAge(self, age):
        self._age = age

    def _createNameView(self, read_only):
        if read_only:
            widget = QLabel(self._name)
        else:
            widget = QLineEdit()
            widget.setText(self._name)
            widget.textChanged.connect(self._updateName)

        return widget

    def _createSurnameView(self, read_only):
        if read_only:
            widget = QLabel(self._surname)
        else:
            widget = QLineEdit()
            widget.setText(self._surname)
            widget.textChanged.connect(self._updateSurname)

        return widget

    def _createAgeView(self, read_only):
        if read_only:
            widget = QLabel(str(self._age))
        else:
            widget = QSpinBox()
            widget.setValue(self._age)
            widget.valueChanged.connect(self._updateAge)

        return widget

    def __str__(self):
        return "Name: {}\nSurname: {}\nAge: {}".format(self._name, self._surname, self._age)
```

Client code can now request the Visual Proxy by issuing:

```python
person = Person(name="John", surname="Smith", age=18)
view = person.visualProxy()
view.show()
```

### Practical Example: Enthought traits

A more streamlined approach to the Visual Proxy design is provided 
by Enthought Traits/TraitsUI. Boilerplate code is removed
installing automatic bindings between Model properties and UI widgets, 
and automatically selecting the appropriate mapping between data types 
and their UI representation.

The Model is defined through type-enforcing python descriptors. 
```python
class Person(HasTraits):
   name = Str
   surname = Str
   age = Range(0, 100)
```

and the Visual Proxy is obtained by invoking `edit_traits()`

```python
person = Person()
ui = person.edit_traits()
```

which results in a window containing two LineEdit and a Slider.
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
      ``Employee.name`` is invariably represented as a string, 
      and its View presentation is an editable textfield widget.
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
a UI for that specific retrieval.

Visual Proxy, on the other hand, is a full fledged foundation
of all Model objects to provide their own View as implicitly 
described by their data.

### Design

Model objects create their own UI for their own attributes

<p align="center">
    <img src="images/visual_proxy/visual_proxy.png" />
</p>

This approach does not violate encapsulation as a get/set Model did, and
takes into account what was exposed above. Each attribute normally
has one specific way it should be represented, and this consistency 
is respected throughout the application. 

These proxies can eventually be made more complex
to support transactions (if we want to undo a change when Cancel is pressed) 
and awareness of their contextual state (e.g. enabled or disabled according to
the state of another proxy)

The message flow is simplified. All of the transaction is between the Visual
Proxy and its backend attribute. Neither the Control nor the user-visible
window are concerned with this transaction. They just respectively coordinate
the creation and hold the visual rendering of the Visual Proxy object.

# Practical Example 

The following practical example represents a boilerplate 
implementation of the design

```python
class Employee:
    def __init__(self):
        self._name = ""
        self._surname = ""

    def visualProxyAttribute(self, attribute, read_only):
        # One can of course get creative with attribute lookup here 
        create_map = {
            "name": self._createName
            "surname": self._createSurname
        }

        return create_map[attribute](read_only)

    def visualProxy(self, read_only):
        # One can of course get creative with attribute lookup here 
        view = QWidget()
        
        create_map = {
            "name": self._createName
            "surname": self._createSurname
        }

        return create_map[attribute](read_only)
    
    def _updateName(self, name):
        self._name = name

    def _updateSurname(self, name):
        self._name = name

    def _createNameView(self, read_only):
        if read_only:
            widget = QLabel()
            widget.setText(self._name)
        else:
            widget = QLineEdit()
            widget.setText(self._name)
            widget.textChanged.connect(self._updateName)

        return widget
        
    def _createSurnameView(self, read_only):
        if read_only:
            widget = QLabel()
            widget.setText(self._surname)
        else:
            widget = QLineEdit()
            widget.setText(self._surname)
            widget.textChanged.connect(self._updateSurname)

            return widget

```

Client code can now request the Visual Proxy and install it in
the window, effectively embedding it in its View::

```python
    self._window.addWidget(self._employee.visualProxy("name", False))
```

### Practical Example: Enthought traits

A more streamlined approach is provided by Traits/TraitsUI




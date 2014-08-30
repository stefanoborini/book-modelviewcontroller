Visual Proxy
------------

Visual Proxy is an approach first presented by Allen Holub in 1999. It
is wildly different from the previous approaches, but definitely contains
interesting ideas. Holub argues the following:

  - It is very rare for the same Model to be represented at the same 
    time in two different ways. 
  - Model representation is not about the Model object per-se, but
    for some specific attributes of that object. These attributes 
    are generally presented in the same way, regardless of where 
    they will appear in the dialogs. For example, ``Employee.name`` 
    is invariably represented as a string, or as an editable
    textfield when writable.
  - All Model designs given until now assume a get/set approach to
    Model state modification. From a strict Object Oriented interpretation,
    getter/setters is a *faux pas* and should be avoided, as they are
    just access to private state in disguise. 
  - Essential separation between Model and View is clumsy to
    achieve in MVC, which does not scale well at the application level.

For the above reasons, Holub proposes that Model objects should create their
own UI for their own attributes::

    class Employee:
        def __init__(self):
            self._name = ""

        def visualProxy(self, attribute, read_only):
            # One can of course get creative with attribute lookup here 
            if attribute == "name":
                if read_only:
                    widget = QLabel()
                    widget.setText(self._name)
                else:
                    widget = QLineEdit()
                    widget.setText(self._name)
                    widget.textChanged.connect(self._updateName)

                return widget
            
            raise AttributeError("Unknown attribute %s" % attribute)
        
        def _updateName(self, name):
            self._name = name

A client View will simply ask the Model for the visual component::

    class View:
        # ...
        def build(self):
            # ...
            self._layout.addWidget(self._employee.visualProxy("name", False))
            # ...


This approach does not violate encapsulation as a get/set Model did, and
takes into account all the considerations exposed above.

The main shortcoming of this approach is that the Model is completely
and utterly dependent on the GUI toolkit. This may have deep implications
for testability, scriptability and reuse. 



Visual Proxy
------------

Visual Proxy is an approach first presented by Allen Holub in 1999. It
derives from PAC, and it is wildly different from the previous approaches, 
but definitely contains interesting ideas. Holub argues the following:

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
  - An Object Oriented system should focus on objects issuing behavior
    requests to one another, with the data staying put. The previous designs
    instead focus on data transfer from the view to the model, and *vice-versa*.


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

A PAC control object will request the Visual Proxy and install it in
the window, effectively embedding them in its widget::

    class Control:
        # ...
        def build(self):
            # ...
            self._window.addWidget(self._employee.visualProxy("name", False))
            # ...


This approach does not violate encapsulation as a get/set Model did, and
takes into account all the considerations exposed above. Each attribute normally
has one specific way it should be represented, and this consistency is desirable
throughout the application. A date attribute may return a calendar, and a speed
attribute may return a gauge. These proxies can eventually be made more complex
to support transactions (if we want to undo a change when Cancel is pressed) 
and awareness of their contextual state (e.g. enabled or disabled according to
the state of another proxy)

The message flow is simplified. All of the transaction is between the Visual
Proxy and its backend attribute. Neither the Control nor the user-visible
window are concerned with this transaction. They just respectively coordinate
the creation and hold the visual rendering of the Visual Proxy object.

The main shortcoming of this approach are the following:
    - the Model is completely and utterly dependent on the GUI toolkit. 
      This may have deep implications for testability, scriptability and reuse. 
    - If the visual proxy contains static parts (such as the "Name" label
      followed by the line editor) the Model objects may also have to deal with
      localization.
    - Logical dependencies between visual components (*e.g.* when this value is
      1, enable that checkbox) must also be moved to the model layer.




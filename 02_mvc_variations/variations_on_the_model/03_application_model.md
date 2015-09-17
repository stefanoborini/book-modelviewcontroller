# Application Model (MMVC)

### Motivation

In Traditional MVC we pointed out that a Model object should not contain GUI
state. In practice, some applications need to preserve and manage state that is
only relevant for visualization. Traditional MVC has no place for it, but we
can satisfy this need with a specialized Compositing Model: the **Application
Model**, also known as Presentation Model. Its submodel, called **Domain Model**, will be kept unaware of such state. 

An Application Model is closer to the View than a Domain Model, and therefore
able to take into account specific needs of the View it is addressing: in a
scrollable area, where only a part of the overall Model is visible it can hold
information about the currently visible portion of the Domain Model, and
suppress those notifications reporting changes in data currently not visible,
preventing a useless refresh. It can also be used to distill information from
multiple Domain Models, producing something that is relevant for its View. For
example, our Domain Model may be made of objects representing the employees in
a company, company departments and so on, in a rather elaborate network. If the
View wants to display a list of employees regardless of the department, maybe
with a checkbox to select them for further processing, it is convenient to have
an Application Model presenting data to the View as a list, gathering the
details from the Domain Model objects (non-graphical information) while at the
same time keeping track and presenting the checkbox state as well (graphical
information). As a drawback, it is much less reusable: multiple Views can
interact with the same Application Model only if they agree on the visual state
representation (e.g. we want both the Dial and the Slider red when over the rpm
limit). 

Some implementations of Application Model push its responsibilities even further
than purely GUI state: it is, quite literally, the model of the application, and it 
is responsible for modifying application state directly on the application itself.
For example, it might enable/disable menus, show or hide widgets, validation
of the events. Most of the visual logic will be responsibility of this model
object, rather than the controllers. This interpretation has deep implications
for the Dolphin Model View Presenter, which will be examined later.

FIXME: Application model represents the GUI state without the GUI.
it contains the logic for enabling/disabling checkboxes, for example.
FIXME: Application model can contain selection.


FIXME: Some logic may not be possible to extract from the View and put into the presentation
model, especially if this logic is deeply rooted in the graphical characteristics of the
visual state. Examples are options that depends on the screen resolution, or the visual positioning
of the mouse within the window. 
### Design

### Practical Example

To present a practical example. imagine
having a Domain Model representing an engine 

```python
class Engine(BaseModel):
   def __init__(self): 
       super(Engine, self).__init__()  
       self._rpm = 0 

   def setRpm(self, rpm):
       if rpm != self._rpm:
           self._rpm = rpm
           self._notifyListeners()

   def rpm(self):
       return self._rpm
```

Initial specifications require to control the revolution per minute (rpm) value
through two Views: a Slider and a Dial. Two View/Controller pairs observe and
act on a single Model 

<p align="center">
    <img src="images/application_model/basic_layout.png"/>
</p>

Suppose an additional requirement is added to this simple application: the Dial
should be colored red for potentially damaging rpm values above 8000 rpm, and
green otherwise.

<p align="center">
    <img src="images/application_model/application_screenshot.png" />
</p>

We could violate Traditional MVC and add visual information to the Model,
specifically the color 

```python
class Engine(BaseModel):
  # <proper adaptations to init method>

  def dialColor(self):
     if self._rpm > 8000:
        return Qt.red
     else:
        return Qt.green
```

With this setup, when the Dial receives a change notification, it can inquire
for both the rpm value to adjust its position and for the color to paint itself
appropriately. However, the Slider has no interest in this information and now
the Engine object is carrying a Qt object, gaining a dependency against GUI.
This reduces reuse of the Model in a non-GUI application.  The underlying
problem is that the Engine is deviating from business nature, and now has to
deal with visual nature, something it should not be concerned about.
Additionally, this approach is unfeasible if the Model object cannot be
modified.  

An alternative solution is to let the Dial View decide the color
when notified, like this 

```python
class Dial(View):
   def notify(self):
       self.setValue(self._model.rpm())
       palette = QtGui.Qpalette()

       color = Qt.green
       if self._model.rpm() > 8000:
           color = Qt.red

       palette.setColor(QtGui.Qpalette.Button, color)
       self.setPalette(palette)
```

Once again, this solution is impractical, and for a complementary reason: the
View has to know what is a dangerous rpm amount, a business-related concern
that should be in the Model. This solution may be acceptable for those limited
cases when the logic connecting the value and its visual representation is
simple, and the View is designed to be agnostic of the meaning of what is
showing to the User. For example, a label displaying negative values in red may
be used to show bank account balances. The real meaning of a negative balance,
the account is overdrawn, is ignored. A better solution would be to have the
BankAccount Model object provide this logic as isOverdrawn(), and the label
color should honor this semantic, not the one implied by the numerical value.

Given the point above, it is clear that the Engine object is the only entity
that can know what rpm value is too high. It has to provide this information,
leaving its visual representation strategy to the View.  A better design
provides a query method ``isOverRpmLimit`` 

```python
class Engine(BaseModel):
   <...>
   def isOverRpmLimit(self):
       return self._rpm > 8000
```

The View can now query the Model for the information and render it appropriately 

```python
class Dial(View):
   def notify(self):
       <...>
       color = Qt.red if self._model.isOverRpmLimit() else Qt.green

       palette.setColor(QtGui.QPalette.Button, color)
       self.setPalette(palette)
```

This solution respects the semantic level of the business object, and allows to
keep the knowledge about excessive rpm values in the proper place. It is an
acceptable solution for simple state.  

With this implementation in place we can
now extract logic and state from Dial View into the Application Model
DialEngine. The resulting design is known as Model-Model-View-Controller

<p align="center">
    <img src="images/application_model/model_model_view_controller.png" />
</p>

The DialEngine will handle state about the Dial color, while delegating the rpm
value to the Domain Model. View and Controller will interact with the
Application Model and listen to its notifications.  Our Application Model will
be implemented as follows. In the initializer, we register for notifications on
the Domain Model, and initialize the color 

```python
class DialEngine(BaseModel):
 def __init__(self, engine):
   super(DialEngine, self).__init__()
   self._dial_color = Qt.green
   self._engine = engine
   self._engine.register(self)
```

The accessor method for the color just returns the current value 

```python
class DialEngine(BaseModel):
    # ...
    def dialColor(self):
        return self._dial_color
```

The two accessors for the rpm value trivially delegate to the Domain Model

```python
class DialEngine(BaseModel):
    # ...
    def setRpm(self, rpm):
        self._engine.setRpm(rpm)

    def rpm(self):
        return self._engine.rpm()
```

When the ``DialController`` issues a change to the Application Model through the
above accessor methods, this request will be forwarded and will generate a
change notification. Both the Slider and the Application Model will receive
this notification on their method notify. The Slider will change its position,
and the Application Model will change its color and reissue a change
notification 

```python
class DialEngine(BaseModel):
    # ...
    def notify(self):
        if self._engine.isOverRpmLimit():  
          self._dial_color = Qt.red
        else: 
          self._dial_color = Qt.green

        self._notifyListeners() 
```

The DialView will handle this notification, query the Application Model (both
the rpm value and the color) and repaint itself. Note that changing the
``self._dial_color`` in ``DialEngine.setRpm``, as in 

```python
class DialEngine(BaseModel):
    # ...
    def setRpm(self, rpm):
        self._engine.setRpm(rpm)

        if self._engine.isOverRpmLimit():  
            self._dial_color = Qt.red
        else: 
            self._dial_color = Qt.green
```

instead of using the ``notify`` solution given before, would introduce the
following problems: 

   - the dial color would not change as a consequence of external changes on
     the Domain Model (in our case, by the Slider)
   - There is no guarantee that issuing ``self._engine.setRpm()`` will trigger a
     notification from the Domain Model, because the value might be the same.
     On the other hand, the Application Model might potentially change
     (although probably not in this example), and should trigger a notification to
     the listeners. Solving this problem by adding a self._notifyListeners call to
     DialEngine.setRpm will end up producing two notifications when the Domain Model
     does issue a notification.


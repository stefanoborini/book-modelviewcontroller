MVC Variation
=============

Traditional MVC is excellent as a starting point for discussion, but by no
means it must be considered the one and only proper way of doing MVC: real
applications are built around its basic concepts, but include plenty of tricks,
extensions and alternative design choices to satisfy the final requirements
while keeping programming complexity as low as possible. Examples of such
requirements include:

   - a modal dialog must allow changing values, but revert them when the Cancel button is pressed.
   - a modeless dialog allows changing values while the change is visible in another window, but must be reverted if “Restore” is pressed.
   - prevent typing of invalid values, for example a string in a line edit supposed to accept only digits will not accept any key presses from non-digits.
   - alternatively, allow invalid entries, but disable the Ok button and mark the incorrect value red.
   - and so on...

As you can see, the complexity of an application made of hundreds of menus,
text input areas and buttons, plus all the possible logical dependencies among
them can grow considerably. Unexpected interactions and strange communication
patterns emerge in the form of bugs or application freezes. Keeping this
communication network well organized and confined by enforcing a structure is
of paramount importance.  In this section we will examine alternative design in
MVC able to deal with more complex use-case scenarios, constrained by
requirements, architectural needs or self-documentation purposes.


Compositing Model
-----------------

**Addressed Need: Aggregation of information from submodels.**

We will create a trivial address book application whose data sources are two
comma-separated (CSV) files and one XML file. The objective is to have a View
that can display data regardless of the number of sources, and that allows
extension to other storage formats without excessive modifications. The final
application is a simple Qt ListWidget with one name and telephone number per
each row

[picture]

The Model layer is composed of three classes: two of them provide readonly
access to each file format (CSV or XML). The third uses the previous two,
manipulating the data for more convenient handling, in this case merging. The
resulting class AddressBook is a Compositing Model: it acts both as a Model for
its View (the AddressBookView) and as a View for its submodels instances

[picture]

The code for class AddressBookCSV is here shown to illustrate the rather
trivial interface supported by all Model objects. The common base class
BaseModel provides notification services by implementing the well known methods
register, unregister, notifyListeners, and the listeners set, as shown in
Traditional MVC. 

::

   class AddressBookCSV(BaseModel):
       def __init__(self, filename):
           super(AddressBookCSV, self).__init__()
           self._filename = filename

       def numEntries(self):
           try:
               return len(open(self._filename, "r").readlines())
           except:
               return 0

       def getEntry(self, entry_number):
           try:
               line = open(self._filename, "r").readlines()[entry_number]
               name, phone = line.split(',')
               return { 'name' : name.strip(), 'phone' : phone.strip()}
           except:
               raise IndexError("Invalid entry %d" % entry_number)


The code for the View is simplified by the fact that there's no Controller. No
modifications are allowed on our Models, so no GUI events need to be handled

:: 

   class AddressBookView(QtGui.QListWidget):
       def __init__(self, model, *args, **kwargs):
           super(QtGui.QListWidget, self).__init__(*args, **kwargs)
           self._model = model

           self._model.register(self)

The notify method extracts data from the Model and repopulates the ListWidget
after clearing it. As a general rule, this method is rather aggressive and may
introduce flickering or loss of selection of the List items. Solving these
issues is beyond the scope of this example. Additionally, the List does not
need regular refresh cycles, because the Models are readonly and parsed only
once at startup

:: 

       def notify(self):
           self.clear()

           for i in range(self._model.numEntries()):
               entry = self._model.getEntry(i)
               string = "%s (%s)" % (entry["name"], entry["phone"])
               self.addItem(string)

Note how the View is agnostic of the actual Model type, and can render data
from either AddressBookCSV or AddressBookXML. This is expected, as we are
programming against an interface.   The Compositing Model class AddressBook
implements the same interface and will therefore be rendered transparently by
the AddressBookView.  The AddressBook class accepts an arbitrary number of
Models at initialization, and registers as a listener on each of them. The
interface expected by AddressBookView is reimplemented, deriving the data from
the composition of the submodels 

::

   class AddressBook(BaseModel):
       def __init__(self, models):
           super(AddressBook, self).__init__()

           self._models = models

           for m in self._models:
               m.register(self)

The total number of entries is trivially the sum of the number of entries provided by each submodel

::

    def numEntries(self):
        return sum([m.numEntries() for m in self._models])


To get a specific entry, we need to map the absolute entry number to the
relative entry number in a specific submodel, keeping into account the number
of elements in each submodel. We define the accumulate routine to compensate
for the lack of it in python2.

::

    def getEntry(self, entry_number):
        def accumulate(l):
            current_total = 0
            res = []
            for i in l:
                current_total += i
                res.append(current_total)
            return res
        accumulated = accumulate([m.numEntries() for m in self._models])
        source_idx = map(lambda x: x <= entry_number,
                         accumulated).index(False)
        try:
            return self._models[source_idx].getEntry(
                                   entry_number - accumulated[source_idx]
                                   )
        except:
            raise IndexError("Invalid entry %d" % entry_number)

Finally, when any of the submodels notify a change, the Compositing Model
should just perform a notification to its listener, in our case the
AddressBookView 

::

    def notify(self):
        self.notifyListeners()

The application main routine creates the three datasource models, and passes
them to the Compositing Model AddressBook, which is then passed to the View

::

   csv1_model = AddressBookCSV("file1.csv")
   xml_model = AddressBookXML("file.xml")
   csv2_model = AddressBookCSV("file2.csv")

   address_book = AddressBook([csv1_model, xml_model, csv2_model])

   view = AddressBookView(address_book)

In this case, the Compositing Model is performing union of homogeneous
information originating from different sources, but this is not the only case
where a Compositing Model can be useful. Another example is to extract relevant
information from different Models and present them in an easy to query Façade.
These Models are normally conceived to simplify access from a View with
specific presentation objectives. 



Model-Pipe-View-Controller
--------------------------

**Addressed Need: Intercept and filter the data flow between Model and View.**


An additional need that may emerge from our addressbook application is to filter out names and sort them alphabetically. A possible design approach would be to include this logic directly into the AddressBook Model, but this approach would not work if we required two Views to observe the  Model, maybe with different search criteria for the filter. The next plausible candidate for hosting this logic is the View, but this can also lead to problems. The View might have a visual understanding of the semantic of the data, for example it knows how to extract a name from the Model and knows where it should go in the GUI, but does not necessarily possess enough logical understanding of the Model or be the most appropriate place to perform extravagant manipulations. Despite the shortcomings, both approaches may be a good compromise depending on the circumstances. 
An alternative approach that cuts through the problem is a Model-Pipe-View-Controller design, a variation of the Compositing Model approach. It introduces an additional Model class, called Pipe, to intercept the data flow between Model and View and add flexibility for data manipulation while in transit. Its concept is similar to a UNIX pipe, and its most common use is for filtering and sorting. 
The Pipe class encapsulates the transformation logic in a dedicated, potentially reusable Model class. Different Pipe classes can be created, each with specific capabilities. To be compatible with the View, a Pipe should implement the same interface of the submodel, eventually extending it for the additional state it might contain. Pipes can also be chained together to perform sequential reduction of data. 
To present a real case implementation of Model-Pipe-View-Controller, we will add two new Pipe classes to the Model layer introduced in the earlier section: one for filtering (AddressBookFilter) and for sorting (AddressBookSorter), as represented in Fig. 5. 
The implementation will also require two separated Views, both contained in the same window: the AddressBookView was introduced in the previous section and will be connected to the Sorter Model as the end point of the Model chain; The FilterView will instead display and modify the filter string, and will connect to the AddressBookFilter Model.
We will explain the motivations for this design later in the explanation. 

[picture]

The AddressBookFilter registers on the filtered Model and holds the current filter string. 

::

   class AddressBookFilter(BaseModel):
       def __init__(self, model):
           super(AddressBookFilter, self).__init__()
           self._filter_string = ""
           self._model = model
           self._model.register(self)

To modify the filter string, we need a setFilter method. When a new string is set, the product of the AddressBookFilter Model is expected to change, so _notifyListeners is called. 

::

    def setFilter(self, string):
        self._filter_string = string
        self._notifyListeners()

The actual filtering is performed on the fly on the underlying data in the numEntries and getEntry methods, which is the usual interface for the Model in the address book application

::

    def numEntries(self):
        entries = 0
        for i in xrange(self._model.numEntries()):
            entry = self._model.getEntry(i)
            if self._filter_string in entry["name"]:
                entries += 1

        return entries

    def getEntry(self, entry_number):
        entries = 0
        for i in xrange(self._model.numEntries()):
            entry = self._model.getEntry(i)
            if self._filter_string in entry["name"]:
                if entries == entry_number:
                    return entry
                entries += 1

        raise IndexError("Invalid entry %d" % entry_number)

Finally, the Filter forwards notifications from its submodel to its listeners

::

    def notify(self):
        self._notifyListeners()

Similarly, the AddressBookSorter is defined to register on a Model for notifications. The current implementation supports only a simple A-z alphabetical sorting, and as such does not need to expose state for changes. Typical examples of possible state would be ascending vs. descending or the sorting key.  The Sorter would then expose setters for all these values, and the View would have to provide supporting widgets to modify them.

::

   class AddressBookSorter(BaseModel):
       def __init__(self, model):
           super(AddressBookSorter, self).__init__()
           self._model = model
           self._model.register(self)
           self._rebuildOrderMap()

       def numEntries(self):
           return self._model.numEntries()

We implement the sorting naively, by walking through the underlying data and building an index-to-index mapping. 

::

    def _rebuildOrderMap(self):
        values = []

        for i in range(self._model.numEntries()):
            values.append( (i, self._model.getEntry(i)["name"]) )

        self._order_map = map(lambda x: x[0], 
                              sorted(values, key=operator.itemgetter(1))
                             )

The mapping is internal state that does not need to be exposed to the View, but must stay synchronized at all times with the underlying Model. Consequently, it must be recomputed every time the underlying Model reports a change

::

    def notify(self):
        self._rebuildOrderMap()
        self._notifyListeners()

We will then use the order map to extract entries in the appropriate order from the underlying Model

::

    def getEntry(self, entry_number):
        try:
            return self._model.getEntry(self._order_map[entry_number])
        except:
            raise IndexError("Invalid entry %d" % entry_number)

Finally, we need a View and Controller to modify the filter string. The View is a QLineEdit with some layouting and labeling. Its signal textChanged triggers the Controller's applyFilter method, so that as new characters are typed in, the Controller will change the filter string. Note how FilterView does not need a notify method: we don't expect the filter string to change from external sources, and QLineEdit is an autonomous widget which keeps its own state and representation synchronized

::

   class FilterView(QtGui.QWidget):
       def __init__(self, *args, **kwargs):
           super(QtGui.QWidget, self).__init__(*args, **kwargs)
           self._initGUI()
           self._model = None
           self._controller = FilterController(self._model)
           self.connect(self._filter_lineedit,
                        QtCore.SIGNAL("textChanged(QString)"),
                        self._controller.applyFilter
                        )
       def _initGUI(self):
           self._hlayout = QtGui.QHBoxLayout()
           self.setLayout(self._hlayout)
           self._filter_label = QtGui.QLabel("Filter", parent=self)
           self._hlayout.addWidget(self._filter_label)
           self._filter_lineedit = QtGui.QLineEdit(parent=self)
           self._hlayout.addWidget(self._filter_lineedit)

We want to delay the setting of the Model after instantiation, so we need a setter method and design View and Controller to nicely handle None as a Model, always a good practice1. The reason for this delayed initialization is that both FilterView and AddressBookView are visually contained into a dumb container. We will detail this point when analyzing the container.

::

    def setModel(self, model):
        self._model = model
        self._controller.setModel(model)

The FilterController needs only the Model, initially set to None by the View.

::

   class FilterController(object):
       def __init__(self, model):
           self._model = model

       def setModel(self, model):
           self._model = model

The applyFilter method simply invokes setFilter on the associated Model, which must be the  AddressBookFilter instance. Due to Qt Signal/Slot mechanism, this method receives a QString as argument, so we need to convert it into a python string before setting it into the Model

::

    def applyFilter(self, filter_string):
        if self._model:
            self._model.setFilter(str(filter_string))

As described early, the final application will have two Views in the same window, one above the other. To achieve this, we need a container widget to layout the two Views. We don't want to convey any misdirection about this container being anything else but a dumb container, so its initializer does not accept the Models. We will instead set the Model on each individual View from the outside through their setModel methods described earlier

::

   class ContainerWidget(QtGui.QWidget):
       def __init__(self, *args, **kwargs):
           super(ContainerWidget, self).__init__(*args, **kwargs)
           self.filterview = FilterView(parent=self)
           self.addressbookview = AddressBookView(parent=self)
           self._vlayout = QtGui.QVBoxLayout()
           self.setLayout(self._vlayout)
           self._vlayout.addWidget(self.filterview)
           self._vlayout.addWidget(self.addressbookview)

To set up the application, there is little variation from the Compositing Model example: we set up the AddressBook Model from the individual submodels.

::

   csv1_model = AddressBookCSV("../Common/file1.csv")
   xml_model = AddressBookXML("../Common/file.xml")
   csv2_model = AddressBookCSV("../Common/file2.csv")
   address_book = AddressBook([csv1_model, xml_model, csv2_model])

The Pipes are then created and chained one after another

::

   address_book_filter = AddressBookFilter(address_book)
   address_book_sorter = AddressBookSorter(address_book_filter)

AddressBookSorter will then be passed to AddressBookView to display the data at the end of the process, and AddressBookFilter will be passed as a Model for FilterView/FilterController to modify the search string

::

   widget = ContainerWidget()
   widget.addressbookview.setModel(address_book_sorter)
   widget.filterview.setModel(address_book_filter)
   widget.show()

Why did we partition the GUI into two Views, instead of having a unified View
attached to the last Model in the chain and containing both the List and the
Filter line edit? This unified View would have to install its Controller to
modify the Filter string on an AddressBookFilter, but the passed Model is an
AddressBookSorter. The Sorter would therefore have to provide a method to
extract its submodel. The unified View would then invoke this method, hope that
the returned Model is a Filter, and finally pass it to the FilterController.
This would fail if the Sorter is removed from the schema, or another Pipe
object is added on either side of the Sorter. Such design is therefore rather
brittle.  A solution with two separated Views give a more flexible, resilient
and cleaner design: the List does not need to know about the nature of its
Model, it just asks for its data; the Pipe chain can be modified without
affecting the View; The FilterView is attached to its natural Model, the
AddressBookFilter, and its Controller can be installed safely without any
fragile traversal of the Pipe chain.


Application Model (MMVC)
------------------------

**Addressed Need: separate visual state from business state. Grant visual state a dedicated Model.**


In Traditional MVC we pointed out that a Model object should not contain GUI state. In practice, some applications need to preserve and manage state that is only relevant for visualization. Traditional MVC has no place for it, but we can satisfy this need with a specialized Compositing Model: the Application Model, also known as Presentation Model. Its submodel, called Domain Model, will be kept unaware of such state. To present a practical example. imagine having a Domain Model representing an engine

:: 
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

Initial specifications require to control the revolution per minute (rpm) value
through two Views: a Slider and a Dial. Two View/Controller pairs observe and
act on a single Model 

Suppose an additional requirement is added to this simple application: the Dial
should be colored red for potentially damaging rpm values above 8000 rpm, and
green otherwise. 

We could violate Traditional MVC and add visual information to the Model, specifically the color 

::

   class Engine(BaseModel):
      <proper adaptations to init method>

      def dialColor(self):
         if self._rpm > 8000:
            return Qt.red
         else:
            return Qt.green

With this setup, when the Dial receives a change notification, it can inquire
for both the rpm value to adjust its position and for the color to paint itself
appropriately. However, the Slider has no interest in this information and now
the Engine object is carrying a Qt object, gaining a dependency against GUI.
This reduces reuse of the Model in a non-GUI application.  The underlying
problem is that the Engine is deviating from business nature, and now has to
deal with visual nature, something it should not be concerned about.
Additionally, this approach is unfeasible if the Model object cannot be
modified.  An alternative solution is to let the Dial View decide the color
when notified, like this

::

   class Dial(View):
       def notify(self):
           self.setValue(self._model.rpm())
           palette = QtGui.Qpalette()

           color = Qt.green
           if self._model.rpm() > 8000:
               color = Qt.red

           palette.setColor(QtGui.Qpalette.Button, color)
           self.setPalette(palette)

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
provides a query method isOverRpmLimit

::

   class Engine(BaseModel):
       <...>
       def isOverRpmLimit(self):
           return self._rpm > 8000

The View can now query the Model for the information and render it appropriately

::

   class Dial(View):
       def notify(self):
           <...>
           color = Qt.red if self._model.isOverRpmLimit() else Qt.green

           palette.setColor(QtGui.QPalette.Button, color)
           self.setPalette(palette)

This solution respects the semantic level of the business object, and allows to
keep the knowledge about excessive rpm values in the proper place. It is an
acceptable solution for simple state.  With this implementation in place we can
now extract logic and state from Dial View into the Application Model
DialEngine. The resulting design is known as Model-Model-View-Controller

The DialEngine will handle state about the Dial color, while delegating the rpm
value to the Domain Model. View and Controller will interact with the
Application Model and listen to its notifications.  Our Application Model will
be implemented as follows. In the initializer, we register for notifications on
the Domain Model, and initialize the color

::

   class DialEngine(BaseModel):
     def __init__(self, engine):
       super(DialEngine, self).__init__()
       self._dial_color = Qt.green
       self._engine = engine
       self._engine.register(self)

The accessor method for the color just returns the current value

::

   def dialColor(self):
      return self._dial_color

The two accessors for the rpm value trivially delegate to the Domain Model. 

::

  def setRpm(self, rpm):
    self._engine.setRpm(rpm)

  def rpm(self):
    return self._engine.rpm()

When the DialController issues a change to the Application Model through the above accessor methods, this request will be forwarded and will generate a change notification. Both the Slider and the Application Model will receive this notification on their method notify. The Slider will change its position, and the Application Model will change its color and reissue a change notification 

::

  def notify(self):
    if self._engine.isOverRpmLimit():  
      self._dial_color = Qt.red
    else: 
      self._dial_color = Qt.green
    self._notifyListeners() 

The DialView will handle this notification, query the Application Model (both the rpm value and the color) and repaint itself. Note that changing the self._dial_color in DialEngine.setRpm(), as in

::

      def setRpm(self, rpm):
         self._engine.setRpm(rpm)

         if self._engine.isOverRpmLimit():  
            self._dial_color = Qt.red
         else: 
            self._dial_color = Qt.green


instead of using the notify() solution given before, would introduce the
following problems: the dial color would not change as a consequence of
external changes on the Domain Model (in our case, by the Slider) There is no
guarantee that issuing self._engine.setRpm() will trigger a notification from
the Domain Model, because the value might be the same. On the other hand, the
Application Model might potentially change (although probably not in this
example), and should trigger a notification to the listeners. Solving this
problem by adding a self._notifyListeners call to DialEngine.setRpm will end up
producing two notifications when the Domain Model does issue a notification.
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





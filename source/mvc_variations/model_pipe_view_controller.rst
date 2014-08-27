Model-Pipe-View-Controller
--------------------------

**Addressed Need: Intercept and filter the data flow between Model and View.**

An additional need that may emerge from our addressbook application is to
filter out names and sort them alphabetically. A possible design approach would
be to include this logic directly into the AddressBook Model, but this approach
would not work if we required two Views to observe the  Model, maybe with
different search criteria for the filter. The next plausible candidate for
hosting this logic is the View, but this can also lead to problems. The View
might have a visual understanding of the semantic of the data, for example it
knows how to extract a name from the Model and knows where it should go in the
GUI, but does not necessarily possess enough logical understanding of the Model
or be the most appropriate place to perform extravagant manipulations. Despite
the shortcomings, both approaches may be a good compromise depending on the
circumstances. 

An alternative approach that cuts through the problem is a
**Model-Pipe-View-Controller** design, a variation of the Compositing Model
approach. It introduces an additional Model class, called **Pipe**, to intercept
the data flow between Model and View and add flexibility for data manipulation
while in transit. Its concept is similar to a UNIX pipe, and its most common
use is for filtering and sorting. 

The Pipe class encapsulates the transformation logic in a dedicated,
potentially reusable Model class. Different Pipe classes can be created, each
with specific capabilities. To be compatible with the View, a Pipe should
implement the same interface of the submodel, eventually extending it for the
additional state it might contain. Pipes can also be chained together to
perform sequential reduction of data.

To present a real case implementation of Model-Pipe-View-Controller, we will
add two new Pipe classes to the Model layer introduced in the earlier section:
one for filtering (``AddressBookFilter``) and for sorting
(``AddressBookSorter``), as represented in Fig. 5. 

.. image:: ../_static/images/ModelPipe/modelpipe-schema.png
   :align: center

The implementation will also require two separated Views, both contained in the
same window: the ``AddressBookView`` was introduced in the previous section and
will be connected to the Sorter Model as the end point of the Model chain; The
``FilterView`` will instead display and modify the filter string, and will connect
to the ``AddressBookFilter`` Model.  We will explain the motivations for this
design later in the explanation. 

The ``AddressBookFilter`` registers on the filtered Model and holds the current
filter string ::

   class AddressBookFilter(BaseModel):
       def __init__(self, model):
           super(AddressBookFilter, self).__init__()
           self._filter_string = ""
           self._model = model
           self._model.register(self)

To modify the filter string, we need a ``setFilter`` method. When a new string is
set, the product of the ``AddressBookFilter`` Model is expected to change, so
``_notifyListeners`` is called. ::

    def setFilter(self, string):
        self._filter_string = string
        self._notifyListeners()

The actual filtering is performed on the fly on the underlying data in the
``numEntries`` and ``getEntry`` methods, which is the usual interface for the
Model in the address book application ::

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

Finally, the Filter forwards notifications from its submodel to its listeners ::

    def notify(self):
        self._notifyListeners()

Similarly, the ``AddressBookSorter`` is defined to register on a Model for
notifications. The current implementation supports only a simple A-z
alphabetical sorting, and as such does not need to expose state for changes.
Typical examples of possible state would be ascending vs. descending or the
sorting key.  The Sorter would then expose setters for all these values, and
the View would have to provide supporting widgets to modify them ::

   class AddressBookSorter(BaseModel):
       def __init__(self, model):
           super(AddressBookSorter, self).__init__()
           self._model = model
           self._model.register(self)
           self._rebuildOrderMap()

       def numEntries(self):
           return self._model.numEntries()

We implement the sorting naively, by walking through the underlying data and
building an index-to-index mapping ::

    def _rebuildOrderMap(self):
        values = []

        for i in range(self._model.numEntries()):
            values.append( (i, self._model.getEntry(i)["name"]) )

        self._order_map = map(lambda x: x[0], 
                              sorted(values, key=operator.itemgetter(1))
                             )

The mapping is internal state that does not need to be exposed to the View, but
must stay synchronized at all times with the underlying Model. Consequently, it
must be recomputed every time the underlying Model reports a change ::

    def notify(self):
        self._rebuildOrderMap()
        self._notifyListeners()

We will then use the order map to extract entries in the appropriate order from the underlying Model ::

    def getEntry(self, entry_number):
        try:
            return self._model.getEntry(self._order_map[entry_number])
        except:
            raise IndexError("Invalid entry %d" % entry_number)

Finally, we need a View and Controller to modify the filter string. The View is
a QLineEdit with some layouting and labeling. Its signal ``textChanged`` triggers
the Controller's ``applyFilter`` method, so that as new characters are typed in,
the Controller will change the filter string. Note how ``FilterView`` does not need
a ``notify`` method: we don't expect the filter string to change from external
sources, and ``QLineEdit`` is an autonomous widget which keeps its own state and
representation synchronized ::

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

We want to delay the setting of the Model after instantiation, so we need a
setter method and design View and Controller to nicely handle None as a Model,
always a good practice [#]_. The reason for this delayed initialization is that
both ``FilterView`` and ``AddressBookView`` are visually contained into a dumb
container. We will detail this point when analyzing the container ::

    def setModel(self, model):
        self._model = model
        self._controller.setModel(model)

The ``FilterController`` needs only the Model, initially set to ``None`` by the View ::

   class FilterController(object):
       def __init__(self, model):
           self._model = model

       def setModel(self, model):
           self._model = model

The ``applyFilter`` method simply invokes ``setFilter`` on the associated Model, which
must be the  AddressBookFilter instance. Due to Qt Signal/Slot mechanism, this
method receives a ``QString`` as argument, so we need to convert it into a python
string before setting it into the Model ::

    def applyFilter(self, filter_string):
        if self._model:
            self._model.setFilter(str(filter_string))

As described early, the final application will have two Views in the same
window, one above the other. To achieve this, we need a container widget to
layout the two Views. We don't want to convey any misdirection about this
container being anything else but a dumb container, so its initializer does not
accept the Models. We will instead set the Model on each individual View from
the outside through their setModel methods described earlier ::

   class ContainerWidget(QtGui.QWidget):
       def __init__(self, *args, **kwargs):
           super(ContainerWidget, self).__init__(*args, **kwargs)
           self.filterview = FilterView(parent=self)
           self.addressbookview = AddressBookView(parent=self)
           self._vlayout = QtGui.QVBoxLayout()
           self.setLayout(self._vlayout)
           self._vlayout.addWidget(self.filterview)
           self._vlayout.addWidget(self.addressbookview)

To set up the application, there is little variation from the Compositing Model
example: we set up the ``AddressBook`` Model from the individual submodels. ::

   csv1_model = AddressBookCSV("../Common/file1.csv")
   xml_model = AddressBookXML("../Common/file.xml")
   csv2_model = AddressBookCSV("../Common/file2.csv")
   address_book = AddressBook([csv1_model, xml_model, csv2_model])

The Pipes are then created and chained one after another ::

   address_book_filter = AddressBookFilter(address_book)
   address_book_sorter = AddressBookSorter(address_book_filter)

``AddressBookSorter`` will then be passed to ``AddressBookView`` to display the data at
the end of the process, and ``AddressBookFilter`` will be passed as a Model for
``FilterView``/``FilterController`` to modify the search string ::

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
brittle. 

A solution with two separated Views give a more flexible, resilient and cleaner
design: the List does not need to know about the nature of its Model, it just
asks for its data; the Pipe chain can be modified without affecting the View;
The ``FilterView`` is attached to its natural Model, the ``AddressBookFilter``,
and its Controller can be installed safely without any fragile traversal of the
Pipe chain.

.. [#] Additionally, when a View or Controller allows to change the Model after
   initialization, it is important that ``setModel`` unregisters the View from the
   old Model, or it will keep sending change notifications. We skip this step
   because we never register for notifications in the first place.


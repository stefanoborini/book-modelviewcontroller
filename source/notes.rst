Notes
=====
Questions and Answers
Should I use a simple container approach (e.g. key/value dictionary with notifications as a model?
A simple container like a key/value dictionary can technically be used as a model, but as the amount of stored data grows, its unstructured nature and access will lead to entangled, inconsistent and undocumented storage. The model will be a “big bag of data” with very little clarity or enforced consistency. Enforcing access through well defined object relations and interfaces is recommended for models beyond the most trivial cases. 
Local models, or one global model?
case: Model changes, but not in the data relevat to the view.
Who performs validation? View? Controller? Model?
Consistency of the data inside the model?
How to report errors in the view?



Old stuff. make it into a blog post.

Another, more complex example of Smart-UI application is the following simple
calculator: a single window contains a display area to show the current state
of the expression, and a set of buttons to input, execute, and cancel the
expression

The implementation relies on a single class, whose initializers sets the
current expression text in a member variable to empty import sys::

   from PyQt4 import QtCore, QtGui

   class Calculator(QtGui.QWidget):
       def __init__(self, *args, **kwargs):
           super(Calculator, self).__init__(*args, **kwargs)

           self._current_text = ""
           self._createGUI()

The initializer also invokes a method to create the visual representation of
the GUI, by creating widgets and layouting them in a proper arrangement, and
finally using Qt mechanisms to trigger a specific method in response to mouse
clicks::

    def _createGUI(self):
        layout = QtGui.QGridLayout(self)

        self._display = QtGui.QLineEdit(self)
        self._display.setReadOnly(True)

        layout.addWidget(self._display, 0, 0, 1, 4)

        self._buttons = {}
        button_labels = [ ["7","8","9","+"],
                          ["4","5","6","-"],
                          ["1","2","3","*"],
                          ["0","=","C","/"]
                        ]  

        for row, row_list in enumerate(button_labels):
            for column, label in enumerate(row_list):
                button = QtGui.QPushButton(label, self)
                self._buttons[label] = button
                layout.addWidget(button, row+1, column)
                self.connect(button, \
                             QtCore.SIGNAL("clicked()"),\
                             self.buttonClicked)

The buttonClicked method translates the user action into an effective
modification of the internal current_text variable, and synchronizes the
displayed text. If the pressed button is the “=”, the expression is evaluated
and the result is stored in the current_text  variable. If a digit is inserted,
its value is appended to the current_text::

    def buttonClicked(self):
        key = self._buttonToKey(self.sender())

        if key == 'C':
            self._current_text = ""
        elif key == "=":
            try:
                self._current_text = str(eval(self._current_text))
            except:
                pass
        else:
            self._current_text = self._current_text + \
                                 self._buttonToKey(self.sender())

        self._display.setText(self._current_text)

    def _buttonToKey(self, button):
        try:
            return [k for k, v in self._buttons.iteritems() 
                               if v == button][0]
        except:
            return ""

The internal variable self._current_text clearly hosts the state of the object,
and it's a prime candidate for refactoring into a Model object. Similarly, the
helper method _createGUI() creates the Calculator interface and is therefore
clearly part of a View role Note how we create the output display, the buttons
for the digits and the operations, and we connect all buttons to the same
method self.buttonClicked. Inside this method, Qt provides the possibility to
detect which button triggered its execution with the .sender() method. The
method buttonClicked is now responsible for converting the button pressed into
an operation to perform or a new digit to be added to the self._current_text.
It also takes care to guarantee self._current_text and the display have the
same content.  The buttonClicked method is performing Controller operations, by
interpreting the user event according to proper logic and modifying the
contents of the internal state. It also takes care of synchronizing the model
and its representation in the View (the display).  class implements querying
and altering of the internal data (stored in self._value) via the getter/setter
pair value()/setValue(). It also implements notification: the register() method
is called by an interested object, which passes itself as argument. The Model
adds it to an internal collection (the self._listeners set) and then
immediately informs it to update itself by means of the call to
listener.notify(). Finally, when data is altered (via setValue), the routine
_notifyListeners() is called, which in turn calls notify() on all registered
listeners.

combining two or more roles on the same class can be an acceptable compromise,
whose cost is a reduction in flexibility and clarity, and whose advantage is a
more streamlined approach for simple cases. Note that mixing the roles does not
imply that the code responsible for each of these roles should mix as well. it
is in fact good practice to keep the code performing each role in separate
routines. This simplifies both understanding and future refactoring, if the
needs emerges. 

following the hierarchic composition of the GUI nesting. The model can be the
same. In pratice, the scheme given above can be simplified by assuming a given
hierarchy talks to the same model In J2EE, this approach is also known as
Composite View.[11] [PIC of an example of a hierarchy with real widgets]




Reimplement widgets to define methods for events. Annoying, proliferates classes.

Once notified, the views are in charge of fetching the new state from the
model: the view must therefore be aware of the model interface and its
semantics. 







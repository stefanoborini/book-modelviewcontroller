Smart-UI: A single class with many responsibilities
---------------------------------------------------

We start this exploration of MVC with the most trivial and simplistic
application: a click counter. This application shows a button with a number.
The number is increased every time the button is clicked. 
    
.. image:: ../_static/images/SmartUI.png
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

The application's main and only visual component, ``Counter``, is derived from
a single GUI class, a Qt ``QPushButton``. The ``Counter`` class holds multiple
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


FIXME also known as autonomous view
combining two or more roles on the same class can be an acceptable compromise,
whose cost is a reduction in flexibility and clarity, and whose advantage is a
more streamlined approach for simple cases. Note that mixing the roles does not
imply that the code responsible for each of these roles should mix as well. it
is in fact good practice to keep the code performing each role in separate
routines. This simplifies both understanding and future refactoring, if the
needs emerges. 

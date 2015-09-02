Smart-UI: A single class with many responsibilities
---------------------------------------------------

We start this exploration toward MVC with the most trivial and simplistic design: **Smart UI**, also known as **Autonomous View**. 

----
**Important**
    
A confusing characteristic of MVC literature is that different names are used to express the same concepts. Vice-versa, it is also common that the same name is used to express totally different concepts. We accept this by proposing the most common names, reporting "also known as" names, and stressing differences when appropriate.

----


The Smart UI approach uses a single class to handle all responsibilities we expect from a GUI program:

   - Receives user driven events, such as mouse clicks and keyboard input
   - Holds application logic to convert user driven events into changes of application state
   - Holds the relevant application state
   - Performs visual rendering of its state

As an example implementation of a Smart UI, consider a click counter application, which shows a button with a number. The number is increased every time the button is clicked. 
  
<p align="center">
  <img src="images/SmartUI.png"/>
</p>  

The code is as follows:

```python
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
```

The application's main and only visual component, ``Counter``, is derived from
a single GUI class, a Qt ``QPushButton``. Observe in particular how ``Counter`` is
    
1. Storing the current click count value in the member variable ``self._value``.
2. Handling the logic that modifies ``self._value``. Every time the button is
   clicked, Qt invokes ``mouseReleaseEvent`` automatically. In this method 
   the click counter is incremented. 
3. Synchronizes the aspect of the button with the current ``self._value``, 
   by invoking ``setText``.

This minimalist design seems appealing for its simplicity and compactness.
It is a good starting point for trivial applications, and the one most likely to
be implemented by novices in GUI programming, but it does not scale well for
larger applications, where state, user events and graphic layout are more
complex and intertwined and need to change often under development pressure. 
Specifically, observe the following issues:

- Access and modification of the current state from outside is cumbersome, being
  contained into the all-encompassing visual object: external objects that want to
  modify the current counter need to make sure that the represented value is
  synchronized, for example, forcing a call to ``_update()``, or having the
  ``Counter`` object provide a ``setValue()`` method.

- It is difficult for other visual objects to report the same information,
  maybe with two different visual aspects (*e.g.* both as a counter and as a
  progress bar)

- The resulting class is difficult to test. The only way to stress it through
  its public interface and functionality is to actually probe it with GUI
  events, which is impractical for reasons we will examine later.

- The logic dealing with visual aspect (i.e. handling and layouting widgets,
  updating the label on the button), interaction aspect (handling the user
  initiated mouse click to perform the increment operation) and business aspect
  (incrementing the counter) are of different nature, and would be better kept
  separated. This would ease testability, simplify code understanding and
  interaction.



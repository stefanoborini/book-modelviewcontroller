MVC Testing
-----------

In general, you should be able to test or even use the model
independently of the controller and views. In fact, the model should
be able to work without any controllers or views implemented at all.
It's a completely separated layer with no dependencies toward GUI
representation, widgets, or strategies to apply the changes. If this
is not the case, then you have a code smell that needs refactoring.
There are however exceptions to this rule [7]. For example, suppose
your model is representing the state of a drawing program. The shapes
that are inserted in the model are actual Shape objects that are
graphical in nature, and it would make sense to assign to these
objects the responsibility of drawing themselves on the view. This is
practical, but it can backfire: it requires the objects to know about
the specific view's details about how to draw itself onto it, meaning
that a different view might not be compatible. Assigning
representation responsibilities to model objects is a rare occurrence
that can always be worked around, for example separating the
mathematical description of the Shape (e.g. the corners of a
rectangle) from the drawing logic (e.g. the actual graphic calls that
draw the rectangle on the screen) and move this drawing logic in a
Renderer class. 


A view that acts on a widget knowing nothing about the model. View
“adapter”

Microsoft Visual Testing
Sending events with xtest, or with the widget level interface.
Sporadics due to change in layout, running the screensaver.

asynchronous tests tend to be slow (you need to perform an action, then
wait for the result that may come and sporadically broken, because
of race conditions.  Favor synchronous testing, restrict asynchronous.

Test of components that are hard to test should be minimal, and the behavior
of these components should be minimal as well.

You can perform tests of graphical components by pushing events into the 
GUI toolkit event queue, but again, they tend to be brittle and asynchronous.

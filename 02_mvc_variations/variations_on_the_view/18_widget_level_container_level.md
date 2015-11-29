# Widget-level vs Container-level MVC

### Motivation

In our previous exploration we defined Views without any detail on the
scope of their implementation. Given a window containing a dozen of widgets, 
two implementations of the View object are possible:
- The View is the full window, forming a single MVC Triad through a complex,
dedicated Controller, or
- Each widget is considered a View. There are multiple independent 
Triads, one per each widget.

Both approaches are possible, and they are called **Container-level** and 
**Widget-level MVC**, respectively. Each solution has advantages and 
disadvantages: Widget-level has the strong advantage of reusability. Views are off-the-shelf UI widgets, and Controllers are generic classes tailored to 
specific widgets. The connection between the widget and the Model property become straightforward, albeit prone to produce boilerplate code to set up the connection. 
With some additional support, the boilerplate can be eliminated, leading to the design known as Data Binding.

On the other hand, a Container level approach may be better suited for multiple
Models and complex cross validation between data, because the cross validation
can be performed by the specialized Controller. 

### Design

A Widget-level design requires one specific controller for each widget of the 
toolkit. Its role is to handle the communication and data conversion between 
the widget and the Model.






is better explained with a practical example
supporting the explanation: a window contains a LineEdit widget to write a 
message and a "Send" button to send the message. The resulting design will have 
two widgets (LineEdit and Button, each of them a View), two specialized 
Controllers (LineEditController and ButtonController) and a single Model.





If you consider widget-level MVC, you should probably investigate Data Binding solutions.

equilibrium between fine-grained per-widget MVC and coarse-grained
per-container MVC. You should generally consider aggregation in these cases:

   * you have a root widget containing a complex set of child widgets.
   * you have a single widget providing an advanced functionality that is 
independent of the functionality of the container.

but it introduces the following shortcomings:
- conversion of data between the Model representation (e.g. float) and the View
representation (e.g. string) could require reimplementation of either the View
or the Model class in some toolkits, or requires specific controllers handing the conversion
- The controller may be too trivial in some cases, in particular with complex
Models (e.g. multiple instances must be handled) or complex Views (e.g.
different widgets that need to be analyzed by the controller at the same time).

### Practical example

: a generic LineEdit could be connected to
a Model string variable via a LineEditStringController, or to a float variable
via a LineEditFloatController. The Controller would take care of validating and
converting the data type (for example, from the string provided by the LineEdit
to a float)

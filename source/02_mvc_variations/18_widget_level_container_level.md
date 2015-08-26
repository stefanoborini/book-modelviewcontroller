Widget-level vs Container-level MVC
-----------------------------------

In our previous exploration we defined Views without much attention on the
scope of their implementation. Should we have multiple minimalistic triads,
where every widget is a View of its triad, or a single MVC triad whose complex
View holds and manages dozen of widgets? Both approaches are possible, and they
are called Widget-level and Container-level MVC, respectively.  Widget-level
MVC favors minimalistic MVC components. Each View is defined by a single
widget, which is connected to the Model through a simple Controller. For
example, a CheckBoxView could be connected to a simple boolean variable in the
Model (True/False, honoring the state of the Checkbox) via a
CheckBoxController. Similar Controllers can be setup for each widget of our
graphic toolkit.
This implementation has several advantages: the connection between the GUI
component and a program variable (or set of variables) is simple and
straightforward, and a relatively limited palette of generic controllers can be
implemented and reused. Specialized Controllers can be developed to address
specific conversions and constraints: a generic LineEdit could be connected to
a Model string variable via a LineEditStringController, or to a float variable
via a LineEditFloatController. The Controller would take care of validating and
converting the data type (for example, from the string provided by the LineEdit
to a float)

[FIXME add code/image]

Although very attractive, Widget-level MVC is not without shortcomings: its
infinitesimal granularity could scale badly for large applications, and
conversion of data between the Model representation (e.g. float) and the View
representation (e.g. string) could require reimplementation of either the View
or the Model class in some toolkits. Another shortcoming is that it only acts
as a data transport from View to Model and vice-versa for a specific widget.
The controller may be too trivial in some cases, in particular with complex
Models (e.g. multiple instances must be handled) or complex Views (e.g.
different widgets that need to be analyzed by the controller at the same time).
One possible solution to these shortcomings is to aggregate different Views
into a single class and keep the MVC triads confined there. The aggregated
class has its own model, and all interaction from outside happens on this local
model.
Widget-level MVC has the disadvantage that leads to class explosion if the
language requires reimplementation of each specific widget. Also, it
complicates design by granting a potentially excessive granularity and
flexibility.

On the other side of the spectrum of Widget-level MVC, Container-level focuses
on Views at the level of containers, and complex Controllers. A View is, for
example, a full dialog. This container holds individual widgets, that are
treated not as individual views, but as a hierarchy of visual components.

Container level is coarse grained, and as such it could become excessively
large.

Given the two choices, it might seem somewhat challenging to select a
particular strategy. The best, as often happens, is to find the right
equilibrium between fine-grained per-widget MVC and coarse-grained
per-container MVC. You should generally consider aggregation in these cases:

   * you have a root widget containing a complex set of child widgets.
   * you have a single widget providing an advanced functionality that is independent of the functionality of the container.

Is better treated as an independent view.

For example, a dialog is best treated as a single view, but if you have a
dialog containing different tabs, each tab content is probably better treated
as an individual view. If you have a complex widget showing a document , which
embeds zoom level (+/-) buttons, they are probably best implemented as either
two separate views, or as a “ZoomLevel” widget as a view, never as a hidden
part of the DocumentViewer View.


With this approach, the application GUI is sliced into manageable parts, each handling a specific User-system interaction. The coarseness of these slices is a matter of choice, circumstances, complexity, and reuse.


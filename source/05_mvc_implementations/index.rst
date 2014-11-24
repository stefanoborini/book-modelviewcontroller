MVC Implementations
===================

Nokia Qt
--------

Qt provides Views and associated Models, who are either tabular or hierarchical
in nature.  The framework also provides derived classes for Views, called
Widgets. Widgets combine View and Model in a single class, allowing to store
data directly into the view. This approach loses flexibility and ease of reuse
of the data contents, but it can be convenient for some specific cases (for
example, if you want to control addition and removal directly on the widget).
Qt has delegates, that are associated to views. Delegates are responsible for
handling controller tasks, and in addition control rendering and editing of
these views. A delegate renders data into the view with the paint() method, and
creates editors for the data with createEditor(). Default Delegates are
installed on every view.  The model contains data classified in roles. Some
roles are purely data oriented, while other roles (FontRole) are view-level
information. The model is therefore responsible for influencing the visual
appearance of thje view through the Role mechanism. Of course, this mechanism
can also be implemented by a specialized delegate who translates the Data
semantic into visual semantic.
 
Controller: establishes connections between model and view
Model: emits signals
view knows the model, and are responsible for changing it. A common, general
interface to the model is used to access data from the views.  It's a
traditional MVC.
Filters: model-pipe-view-controller
MVC model: modification through slots. Notification via signals.

Emitting before changing the data in the model, to track changes. But careful
if the calling code is in another thread.

References [8]

iOS
----
In iOS and cocoa, the MVC is a Model View Adapter style.
Coordinating controllers vs. mediating controllers.


delegates
outlet
data source
notification and Key-Value Observing (KVO)

Java Swing

Model-Delegate
Microsoft
MFC


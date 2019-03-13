---
grand_parent: 2 MVC Variations
parent: 2.5 Variations on the triad
nav_order: 17
---
# 2.5.17 Nokia Qt

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

FIXME: For example, the QListView is a MV counterpart of QListWidget.
There's no controller in Qt, it doesn't need any. In practice, Qt is a
Model Delegate Editor design, except that the Delegate is called View, and
the Editor is called Delegate. Such is life.

MVC model: modification through slots. Notification via signals.

Emitting before changing the data in the model, to track changes. But careful
if the calling code is in another thread.

Qt model sort of a value model, but provides both visual and business data.
The data structure is flexible to accommodate tabular and tree data on the same model
structure.

Specialized models provide access to specific data (e.g. sql table, filesystem directory).
Views are oblivious of the data provider as long as it fulfills the AbstractModel interface.

```python
directory = QDirModel()
table = QTreeView()
tree.setModel(directory)
tree.setRootIndex(directory.index("/")
```


Model indexes are created on the model, acting as a factory. Indexes can mutate as new elements
are added or removed. A Persistent index is available to refer to a specific entry regardless
of modifications to the model.

Model defines row, column and parent. Views don't necessarily use all the degrees of freedom.
For example, a table may not need the parent, or a listView may not need the column, but the
treeview needs all of them


The view requests only the data that it needs to show. This can save considerable time,
and allows the model to do caching strategies or pre-fetching.


Qt also provides sort/filter (Pipe).

Model is a Presentation model.

Complex application models need to be adapted into Qt models if needed.
In a sense, the Qt model is an adaptor to a data representation (both visual and
business) that is appreciated by the Views provided by qt.
With more complex views, or models, the Qt mechanism breaks down, because it's
finalized at a very specific data organization and visualization mechanism.

Provides the following Models


QStringListModel: Stores a list of strings
QStandardItemModel: Stores arbitrary hierarchical items
QFileSystemModel:  Encapsulate the local file system
QSqlQueryModel: Encapsulate an SQL result set
QSqlTableModel: Encapsulates an SQL table
QSqlRelationalTableModel: Encapsulates an SQL table with foreign keys
QSortFilterProxyModel: Sorts and/or filters another model

QAbstractItemModel

and the following Views

QColumnView, QHeaderView, QListView, QTableView, and QTreeView.
QAbstractItemView

The Qt MVC is simple and aimed at specific data representation and
visualization. It's not a general framework for MVC.


Delegates:

Factories for editors. createEditor() method can be reimplemented to return
a specific widget that can edit a given cell in the model.
It also has the gateway routines model->editor and editor->model for the data
transit: setEditorData and setModelData. They are called at the beginning of the edit
and at the end.
It also provides the rendering logic for the element: method paint()


# Data Dialog

### Motivation

Data Dialog is a simplified and practical design to retrieve information from the User
by means of a Dialog. It is generally used for Preference dialogs.

To use a Data Dialog, the following constraints must be respected:

 - It must be Modal (i.e. when visible, interaction with the rest of the application is prevented)
 - It only allows Accept (``Ok`` button) and Reject (``Cancel`` button) operations, not Apply.
 - It does not need to synchronize with the application state while visible.

Testability of the Data Dialog itself is potentially complex due to its synchronous nature.
Client code however can replace Data Dialog with a mock honoring the same interface,
resulting in easier testability of this part of the application.

This design is different from the Local Model.
A local model is a real Model that is connected to the View through notification,
but has simply been copied to preserve its older state in case the changes are
reverted. Data dialog, on the other hand, is simply a View with an API to
accept data to populate its widgets, or retrieve their content in a trivial
representation.

### Design

Data dialog's widgets are populated through an appropriate method call, passing
data with a trivial representation.
The Data Dialog ``show`` operation must be blocking on the invoking code.
Once invoked, Data Dialog extracts the information from the passed Model and
populates its widgets accordingly.

Next, a DataDialog object is instantiated, and the gathered data
is passed at initialization; Widgets in the DataDialog are populated
accordingly with the passed data, and the dialog is then shown modally to the
User.

With the dialog now visible, the User can modify the presented values, with
validation performed on the Dialog class. Eventually, the User will issue
either an "Ok" or "Cancel". With an "Ok", the new data is gathered from the
Dialog, processed by the backend and applied to match the changed options.
With "Cancel", the gathered information is simply discarded.

Alternative designs can return the changed information only, or
let the client code extract the information from the dialog's widgets, although
the latter is impractical.

### Practical Example

The following example with Qt will show the main concept outlining Data Dialog.
Both idiomatic python and Qt have been ignored to favor clarity, as usual.

The ``DataDialog`` class implements a Dialog with textual fields, an Ok and Cancel buttons.

```python
class DataDialog(QDialog):
    def __init__(self, parent=None, flags=0):
        super(DataDialog, self).__init__(parent, flags)
        self._line_edits = {}
        self._data_fields = ["name", "surname", "age"]

        layout = QGridLayout()
        for row, field in enumerate(self._data_fields):
            layout.addWidget(QLabel(field), row, 0)

            line_edit = QLineEdit()
            layout.addWidget(line_edit, row, 1)

            self._line_edits[field] = line_edit

        ok = QPushButton("Ok")
        cancel = QPushButton("Cancel")
        self.connect(ok, SIGNAL("clicked()"), self.accept)
        self.connect(cancel, SIGNAL("clicked()"), self.reject)
        layout.addWidget(cancel, len(self._data_fields), 0)
        layout.addWidget(ok, len(self._data_fields), 1)

        self.setLayout(layout)
```

The core of the design resides in the ``set_content/get_content`` pair:
``set_content`` accepts a dictionary with appropriate data for the dialog
fields, and fills the widgets with its contents. ``get_content`` retrieves
the data from the widgets and returns them as a dictionary to the client code.

```python
class DataDialog(QDialog):
    # <...>
    def set_content(self, data):
        for field in self._data_fields:
            line_edit = self._line_edits[field]
            if field in data:
                line_edit.setText(data[field])

    def get_content(self):
        data = {}
        for field in self._data_fields:
            line_edit = self._line_edits[field]
            data[field] = line_edit.text()

        return data
```

The client code interacts with the dialog by setting and retrieving the
data through these two methods:

```python
data = {"name": "Albert",
        "surname": "Einstein",
        }

data_dialog = DataDialog()
data_dialog.set_content(data)

if data_dialog.exec_() == QDialog.Accepted:
    print("Dialog Accepted. Content:")
    print(data_dialog.get_content())
else:
    print("Dialog Canceled.")
```



import sys
from PySide.QtCore import SIGNAL
from PySide.QtGui import QDialog, QApplication, QGridLayout, QLabel, QLineEdit, QPushButton


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


class ApplicationView(QPushButton):
    def __init__(self, parent=None, flags=0):
        super(ApplicationView, self).__init__(parent, flags)
        self.connect(self, SIGNAL("clicked()"), self._clicked)

    def _clicked(self):
        data = {"name": "Albert",
                "surname": "Einstein",
                }

        data_dialog = DataDialog()
        data_dialog.set_content(data)

        if data_dialog.exec_() == QDialog.Accepted:
            print(data_dialog.get_content())
        else:
            print("Dialog Canceled")


app = QApplication(sys.argv)
view = ApplicationView()
view.show()

app.exec_()


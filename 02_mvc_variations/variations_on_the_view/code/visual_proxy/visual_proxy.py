import sys
from PySide.QtGui import QWidget, QApplication, QGridLayout, QLabel, QSpinBox, QLineEdit

class Person:
    def __init__(self, name="", surname="", age=0):
        self._name = name
        self._surname = surname
        self._age = age

    def visualProxyAttribute(self, attribute, read_only=False):
        create_map = {
            "name": self._createNameView,
            "surname": self._createSurnameView,
            "age": self._createAgeView,
        }

        return create_map[attribute](read_only)

    def visualProxy(self, read_only=False):
        view = QWidget()
        layout = QGridLayout()
        for row, attr in enumerate(["name", "surname", "age"]):
            layout.addWidget(QLabel(attr), row, 0)
            layout.addWidget(self.visualProxyAttribute(attr, read_only), row, 1)
        view.setLayout(layout)
        return view

    def _updateName(self, name):
        self._name = name

    def _updateSurname(self, surname):
        self._surname = surname

    def _updateAge(self, age):
        self._age = age

    def _createNameView(self, read_only):
        if read_only:
            widget = QLabel(self._name)
        else:
            widget = QLineEdit()
            widget.setText(self._name)
            widget.textChanged.connect(self._updateName)

        return widget

    def _createSurnameView(self, read_only):
        if read_only:
            widget = QLabel(self._surname)
        else:
            widget = QLineEdit()
            widget.setText(self._surname)
            widget.textChanged.connect(self._updateSurname)

        return widget

    def _createAgeView(self, read_only):
        if read_only:
            widget = QLabel(str(self._age))
        else:
            widget = QSpinBox()
            widget.setValue(self._age)
            widget.valueChanged.connect(self._updateAge)

        return widget

    def __str__(self):
        return "Name: {}\nSurname: {}\nAge: {}".format(self._name, self._surname, self._age)

app = QApplication(sys.argv)
person = Person(name="John", surname="Smith", age=18)
view = person.visualProxy()
view.show()

app.exec_()
print(person)


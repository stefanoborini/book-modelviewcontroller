import sys
from PySide.QtGui import QWidget, QApplication, QGridLayout, QLabel, QSpinBox, QLineEdit

class Person(object):
    def __init__(self, name="", surname="", age=0):
        self._name = name
        self._surname = surname
        self._age = age

    def visual_proxy(self, read_only=False):
        view = QWidget()
        layout = QGridLayout()
        for row, attr in enumerate(["name", "surname", "age"]):
            layout.addWidget(QLabel(attr), row, 0)
            layout.addWidget(self.visual_proxy_attribute(attr, read_only), row, 1)
        view.setLayout(layout)
        return view

    def visual_proxy_attribute(self, attribute, read_only=False):
        method = getattr(self, "_create_{}_view".format(attribute))
        return method(read_only)

    def _update_name(self, name):
        self._name = name

    def _update_surname(self, surname):
        self._surname = surname

    def _update_age(self, age):
        self._age = age

    def _create_name_view(self, read_only):
        if read_only:
            widget = QLabel(self._name)
        else:
            widget = QLineEdit()
            widget.setText(self._name)
            widget.textChanged.connect(self._update_name)

        return widget

    def _create_surname_view(self, read_only):
        if read_only:
            widget = QLabel(self._surname)
        else:
            widget = QLineEdit()
            widget.setText(self._surname)
            widget.textChanged.connect(self._update_surname)

        return widget

    def _create_age_view(self, read_only):
        if read_only:
            widget = QLabel(str(self._age))
        else:
            widget = QSpinBox()
            widget.setValue(self._age)
            widget.valueChanged.connect(self._update_age)

        return widget

    def __str__(self):
        return "Name: {}\nSurname: {}\nAge: {}".format(self._name, self._surname, self._age)

app = QApplication(sys.argv)
person = Person(name="John", surname="Smith", age=18)
view = person.visual_proxy()
view.show()

app.exec_()
print(person)


#!/usr/bin/env python
# SmartUI example. A trivial calculator class. Note how
# GUI handling, business logic and interaction are all
# handled by one class.
# By Stefano Borini 2013. CC-SA
# NOTE: Not using Qt features (signal/slots) on purpose.

import sys
from PyQt4 import QtCore, QtGui


class Calculator(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(Calculator, self).__init__(*args, **kwargs)

        self._current_text = ""
        self._createGUI()

    def _createGUI(self):
        layout = QtGui.QGridLayout(self)

        self._display = QtGui.QLineEdit(self)
        self._display.setReadOnly(True)

        layout.addWidget(self._display, 0, 0, 1, 4)

        self._buttons = {}
        button_labels = [ ["7","8","9","+"],
                          ["4","5","6","-"],
                          ["1","2","3","*"],
                          ["0","=","C","/"]
                        ]

        for row, row_list in enumerate(button_labels):
            for column, label in enumerate(row_list):
                button = QtGui.QPushButton(label, self)
                self._buttons[label] = button
                layout.addWidget(button, row+1, column)
                self.connect(button, QtCore.SIGNAL("clicked()"), self.buttonClicked)

    def buttonClicked(self):
        key = self._buttonToKey(self.sender())

        if key == 'C':
            self._current_text = ""
        elif key == "=":
            try:
                self._current_text = str(eval(self._current_text))
            except:
                pass
        else:
            self._current_text = self._current_text + self._buttonToKey(self.sender())

        self._display.setText(self._current_text)

    def _buttonToKey(self, button):
        try:
            return [k for k, v in self._buttons.iteritems() if v == button][0]
        except:
            return ""

app = QtGui.QApplication(sys.argv)

# Initialize
calculator = Calculator()

# Show and exec the event loop
calculator.show()
app.exec_()

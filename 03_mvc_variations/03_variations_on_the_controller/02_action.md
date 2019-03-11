---
grand_parent: MVC Variations
parent: Variations on the Controller
summary: Controller with visual representation encapsulating a command.
nav_order: 2
---
# Action

### Motivation

User interfaces often require a given operation to be available from different points of
access: the menubar, contextual menus, toolbars, and keyboard accelerators. 
An effective design choice to handle this use case is to define an **Action**,
a pluggable entity encapsulating Command behavior and visual/UI related information,
such as its icon, tooltip, keyboard accelerator, enabled status and so on.

### Design

An Action is peculiar in design characteristic, combining design features of 
Command, Controller, and Model. 

Like a Command, an Action normally provides an abstract method ``triggered()``
to reimplement with the required behavior.  Alternative strategies not
requiring subclassing allow to register a callback that is executed when the
action is triggered. Differently from a Command, the Action is more liberal in
performing UI operations, such as showing a dialog, while Commands generally
act exclusively on Models.

Actions are also both Controllers and visual Models: different Views accept the
same Action and visually represent it in a different way. For example, a
MenuBar might represent it as an icon followed by a title, a ToolBar might
display just the icon and a tooltip, and the application as a whole might not
represent it visually, but activate it when its keyboard shortcut
accelerator is invoked.  Information about the visual aspect of the Action are
contained in the Action itself, fulfilling a Model-like role for this
information. 

Views supporting Actions are generally a form of visual container (e.g.
Menubar, Toolbar) and provide an interface to add and remove them.

### Practical Example

Qt supports a regular example of Action with the QAction class. 
QAction exposes a ``triggered`` Signal that is emitted when the Action is 
activated. This Signal can then connected to any slot callback, where actual
Controller behavior takes place.

```python
menubar = self.menuBar()
toolbar = self.addToolBar('Toolbar')
file_menu = menubar.addMenu('&File')

quit_action = QAction(QtGui.QIcon('quit.png'), '&Quit', self)        
quit_action.setShortcut('Ctrl+Q')
quit_action.triggered.connect(qApp.quit)

file_menu.addAction(quit_action)
toolbar.addAction(quit_action)
```

In this example, we created an Action for quitting the application, then add it
to both the File menu entry and the toolbar. Clicking on either entry, or using
the Ctrl+Q accelerator, will invoke qApp.quit() and quit the application.

# Action

### Motivation

User interfaces often require a given operation to be available from different points of
access: the menubar, contextual menus, toolbars, and keyboard accelerators. 
An effective design choice to handle this use case encapsulates the operation into a 
pluggable entity, the **Action**. The action encapsulates both Controller behavior

It is similar to a Command, but with the substantial differences:

- Command generally acts only on the Model. An action can perform UI operations 
  (such as showing a dialog).
- Command is generally Model support, and holds no UI concerns. Action must support
  purely UI concerns (e.g. the Icon to put in the toolbar, or the keyboard accelerator,
  if it's enabled or not)

Special controller that has different visual aspects and takes care of performing
actions on models. Typically used for menu + toolbar icon. "command-like" together
with pluggable aspect details (icon, text)

### Design

An action is similar in design to a Command: an abstract method ``triggered()`` 
can be reimplemented to provide the required Controller behavior. Alternative strategies
not requiring subclassing allow to register a callback that is executed when the action
is triggered.


### Practical Example

Qt supports a regular example of Action with the QAction. Instead of allowing
to reimplement the behavior, QAction exposes a Signal that is emitted when the
action is triggered. This Signal can then connected to any slot callback, where
actual Controller behavior takes place.


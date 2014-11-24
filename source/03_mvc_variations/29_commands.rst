Commands
--------

**Addressed Need: Undo/Redo and alternative notification strategy.**

Graphical interfaces generally provide Undo/Redo capabilities. This is
generally and easily implemented with the Command pattern. The controller,
instead of directly performing an operation on the Model, will instantiate a
Command object out of a palette of possible Commands. The command object will
be instantiated by passing a reference to the Model. This object will normally
have two methods execute(), and undo(). The Controller will instantiate the
command, and submit it to a Tracking object. The tracking object will call
execute() on the Command, and immediately push it into a stack. The Tracking
will have two stacks, one for undo, and the other for redo. When the user
selects undo, the Tracker will be requested to pop one command from the undo
stack, call its redo() method, and push the command in the redo stack.  Redo
can be implemented by undoing the actual process, or by storing the old state
and reverting it. The memento pattern is here useful to save the state of the
Model before modification, but of course it can be demanding in memory
occupation. 



Using the command pattern to modify the model.  The model can be a factory for
the commands.  The command can perform notification of the listeners instead of
the model.  Another form of qualification: the model forwards the command after
execution to the View. Views can analyze the command to respons appropriately.

a command class normally has execute() and undo() methods. it's a functor.

execute does a given action. undo restores the state as it was before.
undo can be done either by algorithmic rollback, or by just restoring a
memento saved at execute time.

The parameters are defined at instantiation time. execute accepts no parameters
but it may return a state (success, failure). This state will be needed to decide
what to do with the executed command (add to the undo queue or not).

two stacks: undo queue and redo queue. 

execute()
push into undo

at undo:
pop from undo
command.undo()
push into redo

at redo
pop from redo
command.execute()
push into undo

Association of the command to the model: the model defines and offers creation of commands.
The command can also acts as a notification agent (e.g. syncs the view) instead of the model
and can also act as a change object.




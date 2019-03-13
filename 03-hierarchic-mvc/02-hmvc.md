---
parent: 3 Hierarchic MVC
nav_order: 2
---
# 3.2 Hierarchic Model View Controller (HMVC, Recursive MVC)

Hierarchic MVC is a strategy to apply MVC in large applications while keeping
control of the granularity of data and communication. HMVC deploys a hierarchy
of triads by connecting controllers. The triads work together by handling
events they can handle, and forwarding them up in the hierarchy when they don't
know how to handle

[IMAGE]

There are relevant differences when compared with traditional MVC:
the view is responsible for handling user input events. These events are
forwarded to the controller.  The controller as usual performs modification on
the model through direct method call on model objects To refresh the view
state, the controller notifies the view that it needs refresh. The view then
communicates directly with the model, pulling the data from it without
involving the controller further. [4] Alternatively, the model notifies the
view by providing its own state [5] The controller also acts as a hub in the
controller hierarchy. If a controller receives an event from its associated
view that cannot be handled, it is bubbled to the parent, which in turn can
choose to handle it or delegate it further up or down in the tree.  Any model
at any level in the hierarchy can access data at any scope, and models can also
talk to each other. Controllers at any level in the hierarchy can share these
models.

controller has another controller as view
controller handle multiple views or multiple sub controllers

View-model in a observer pattern


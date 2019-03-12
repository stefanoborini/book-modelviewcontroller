---
parent: Hierarchic MVC
nav_order: 1
---
Controller hierarchy in Traditional MVC
---------------------------------------

In order to handle the user events, traditional MVC had to organize controllers
in a hierarchy. When a View received an event, it was handed out to its controller
. Events are delivered according to the actual cursor presence (which basically
indicates which View is in Focus) until they rare given to a controller that is
willing to handle the event.

only one controller active at a time.

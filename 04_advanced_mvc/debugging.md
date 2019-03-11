---
parent: Advanced MVC
---
# Debugging

Hard because:
- Can't see the chain of events. Once the event is delivered and the event loop dispatches it,
  a cascade of calls traverses the tree up and down and up again, making it very hard to 
  understand how the state changes. This is also very hard to deduce by looking at the code.
  Sequentiality is hard to understand because delivery of observer calls are often in arbitrary
  order, or if it isn't, it depends on the order of the listener registration and it is
  unlikely to be explicit. Handlers should therefore not rely on order of change notification
  for the same notification.

the more complicated the network of listeners/notifiers, the harder is to follow the logic.

Techniques for debugging?

---
parent: Advanced MVC
---
# Throttling

### Motivation

Similar to debouncing, but the notification is issued immediately, and then 
not anymore until the timer expires. At the end of the timer, however,
a check must be performed if the current value is different from the 
value issued at the first notification. If different, a new final notification must be issued,
otherwise the View would sit desynchronized from the Model.


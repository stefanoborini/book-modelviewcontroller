---
grand_parent: 4 Advanced MVC
parent: 4.5 Multithreading, async and the event loop
nav_order: 13
---
# 4.5.3 Throttling

### Motivation

Similar to debouncing, but the notification is issued immediately, and then 
not anymore until the timer expires. At the end of the timer, however,
a check must be performed if the current value is different from the 
value issued at the first notification. If different, a new final notification must be issued,
otherwise the View would sit desynchronized from the Model.


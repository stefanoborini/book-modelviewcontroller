---
grand_parent: Advanced MVC
parent: Common Problems
nav_order: 5
---
# Trashing prevention

To prevent trashing with many notifications, there are three strategies:

    - disable notifications, to the operations, re-enable the notifications.
      this has the disadavantage that you might not know what notifications to 
      send when they are re-enabled. One solution could be to spool them,
      and at re-enable, merge the duplicates and send out the minimum.
    - have coarse grained operations, operating on large sets and sending out 
      only one notification at the end.
    - Have fine grained modification routines with an option notify that allows
      to decide when to send the notification and when not to.
    - Have the model be a centralizer of the notification delivery, but have notifyObserver called
      externally. 
    - have a smart signal that can be put in a "trasaction on" mode, and accumulates the
      notifications, and then release the notification when a "commit" is issued



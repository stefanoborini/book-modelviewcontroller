---
grand_parent: 4 Advanced MVC
parent: 4.4 Common Problems
nav_order: 7
---
# Lapsed Listener Problem

A notification system introduces a potential for memory leaks known as
"Lapsed listener problem". It occurs when a listener registers to a
notifier, then goes out of scope without unsubscribing. The listener
is never garbage collected due to the permanence of the notification 
connection. It is technically still receiving notifications, which may introduce
additional problems if these notifications are expensive to honor.
In languages without GC, if the listener is deleted, the notifier can now hold a
reference to freed memory, potentially resulting in a crash.

There are various options to solve this problem. The first is to make sure
the listener is correctly unregistered before going out of scope or released.

The second option is to have a notification system using weak references.

problem can exist also with callbacks that are closures, or when exceptions are
stored. 



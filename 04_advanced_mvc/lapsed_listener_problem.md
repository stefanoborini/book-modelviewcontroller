# Lapsed Listener Problem

A notification system introduces a potential for memory leaks known as
"Lapsed listener problem". It occurs when a listener registers to a
notifier, then goes out of scope without unsubscribing. The listener
is never garbage collected due to the permanence of the notification 
connection. It is technically still receiving notifications, which may introduce
additional problems if these notifications are expensive to honor.

There are various options to solve this problem. The first is to make sure
the listener is correctly unregistered before going out of scope or released.

The second option is to have a notification system using weak references.



# Multithreading

Problem with multiple threads.
Sending notifications that are delivered as the same thread.
Describe how Qt manages to handle delivery through the event loop
if two objects have different thread affinity.

Do not spawn threads. makes things harder to handle. use a thread pool.

Models should be synchronous, so you can decide which threading strategy
to use.

Have futures.

Separate threads can act independently, produced by code running in the main
(event loop) thread. The problem is that any change they can do can propagate 
through the network, and touch parts of the code that is currently handled by the 
main thread. As a result, the generally better way of handling this situation is
that secondary threads communicate with the main thread in two ways:
- setting state (using locks for synchronization)
- posting events into the event loop, so that the main thread can handle them.


Once an event is triggered, the application has around 1/60th of a second to return
control to the event loop, meaning that the object/notification network traversal
must be over quickly. If any event triggers something that can potentially last for more
than the mentioned amount of time, it must be executed in a separate thread, or the
interface responsiveness will suffer.
Having a separate thread carries its additional quirks: can't normally touch ui code,
must be synchronized.

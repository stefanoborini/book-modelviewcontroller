# Multithreading

Problem with multiple threads.
Sending notifications that are delivered as the same thread.
Describe how Qt manages to handle delivery through the event loop
if two objects have different thread affinity.

Do not spawn threads. makes things harder to handle. use a thread pool.

Models should be synchronous, so you can decide which threading strategy
to use.

Have futures.

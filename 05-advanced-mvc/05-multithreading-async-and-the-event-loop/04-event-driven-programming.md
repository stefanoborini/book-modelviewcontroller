---
grand_parent: Advanced MVC
parent: Multithreading, async and the event loop
nav_order: 4
---
# Interaction with the event loop

Until now, very limited mention was made about the event dispatch mechanism
and the event loop: we remained oblivious of how UI events were delivered to the
View/Controller. In the following pages we will examine how events are dispatched
and how crucial is a proper coexistence between the dispatch mechanism and MVC.

In the most simple terms, an event-driven UI program is built on top of an *event
loop*. This infinite loop generally performs these operations:

1. awaits for low level events, like a mouse click, a key press, or a request to show from the windowing system.
2. puts these events in a queue
3. fully consumes the queue and dispatches the events to the appropriate
   handler (e.g. a method on the widget currently in focus). 
   In this phase the thread will traverse, among other things, your MVC.
4. Return to 1.

This loop is executed by the main thread of the program, which then  
executes during a single iteration of the event loop can be extremely complex, and traverse
the complex notification network of your MVC application. The event handler is, for all purposes,
atomic. When it starts, it is the only part of your code that will be executed, and will run to completion
with no chance for interruption.
It is therefore critical, for the application to be responsive to subsequent events waiting 
in the next iteration of the loop, that an event is fully handled within 200 milliseconds.

The consequence of this requirement is that anything in your MVC code that blocks the
executing thread will prevent the event loop to roll, and will slow down or
freeze your application, offering a suboptimal user experience.

Examples of situations where the above may occur are the following:

- initiating a network connection (which may block until a timeout is reached)
- waiting for a state machine to switch state (e.g. become idle)
- a long running computation
- reading or writing a large file either from the disk or from a network connection
- running an external process that must be controlled, or whose stdout must be parsed.

You can see the event loop as a cooperative multitasking system. A cooperative multitasking
system is a system allowing multiple tasks to run, provided that each task relinquish control
when done, giving other tasks the chance to run.

To keep interface responsiveness, you must create a secondary thread of execution
in your program, when the event handler expects to wait. The main thread spawns 
the secondary thread. The secondary thread executes the long running 
task, while the main thread can return to the event queue and keep processing
events. This solution now faces the following difficulties:

- the secondary thread must notify its completion to the main thread, either successfully
  or with an error condition.
- the secondary thread must interact nicely with the main thread. Both threads could access
  the same shared state, for which synchronization is needed
- as a corollary of the above, the secondary thread should not call the event loop or
  any part of the code the main thread is fundamentally responsible for (such as UI handling)
  because it is probably not designed to be thread safe.
- the secondary thread could potentially trigger notifications through MVC (for example, by
  modifying a model state). The notification will propagate to View and Controller classes,
  which may involve UI, which again is not designed for being used by a secondary thread.

As you can see, handling multithreading in an event driven system is not trivial.

An alternative approach to what presented above is suspended execution. 
The concept requires the language to support suspending a routine execution and 
relinquish control back to the caller. When the suspended routine is reinstated,
it will continue from where it left. 

Suspended execution allows a handler to relinquish control back to the event loop,
allow for other events to be processed, and restart where it was. This approach has the following
drawbacks

- it requires language support (e.g. yield keyword in python)
- event handlers are no longer atomic. Processing other events might imply that the restarting
  handler is now handling a state that may no longer be consistent. A point of yield can be seen as
  a point where any code can be arbitrarily executed.
- Does not solve for blocking calls, but may allow for event processing if the suspendable task 
  can be broken down into chunks, where one can periodically relinquish control (e.g. a loop).

This approach is equivalent to calling the processEvents manually at the point of yield.

For the blocking calls, the ideal solution would be to have a routine that acts as non-blocking
and notifies back when completed. This is the case of a callback, a routine that gets called
when the secondary thread has completed its task. The most common problem of this approach is
that the callback will be executed in the secondary thread as well, so in general it cannot perform
any action that may conflict with the main thread. The recommended course of action is that
the secondary thread, now running the callback, notifies the main thread through an event.
Event queues implementations are generally aware of this need and are therefore thread safe.




--------------------


MVC was considered as an independent design approach without much consideration
of the event system. Strictly speaking, MVC does not require an event loop, but its usefulness
would be severely limited.


Explain how MVC naturally ends up with an event driven model.
Explain the complexity of debugging (e.g. backtraces all coming from the event
loop)

Behavior is no longer characterized by code alone. Emergent behavior arises from
the potentially asynchronous interaction among objects, communicating through
events. The communication network being mutable. This results in extremely 
complex, hard to understand, hard to debug designs.



solve this?  One solution is to spawn another thread, and let this other thread
do the heavy, long running work, while the main thread goes back to the event
loop and keeps processing events. But multithread programming is hard, and
event driven multithread programming even more so.
So ideally, you would prefer to have a single thread, but when it encounters
something that is long running, you use a trick to suspend the execution point,
and resume it later, when the long running task is completed, or maybe you want
to do it in steps, each one short, but taken together they run for a long time.
the yield keyword, and therefore generators, happen to provide this exact
service: suspend something and resume it later from where you left it.  When
you reach the yield, the main thread can now go back to the event loop, and
keep processing events. Somehow, where the execution was suspended to wait for
a long running thing there will be some magic so that when the long running
thing is done, the thread will know about it and go back to where it was
suspended. This can be achieved either by a secondary thread, or by the main
thread itself: when it runs out of events to process, it works on the long
running task, maybe to be suspended again a little later.  What you see is what
is known as collaborative (or cooperative) multitasking. The event loop is
basically a "kernel", and yield points are equivalent to "system calls" into
the "kernel". At this yield points, the control is returned to the kernel,
which is now free to run something else, interleaving all the handling and
keeping the event processing alive, instead of being stuck at one particular
handler. Note that this mechanism requires collaboration: the individual
handlers must yield to inform the "kernel" "I'm not done here yet, but give
someone else a chance to keep going". This compares with preemptive
multitasking where the kernel is the one saying: "that's it, you had enough
fun, let's someone else go now", which is what modern real kernels do.  So
asyncio is a form of event loop and collaborative multitasking to allow event
driven programming without either having an unresponsive application or having
to deal with multiple threads, callbacks and all the horror that arises from it
in an event driven environment.

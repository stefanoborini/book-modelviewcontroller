---
parent: Advanced MVC
---
# Delayed Model

FIXME: Asynchronous.  Move this one to advanced patterns. 

### Motivation


Every time a Model changes, the View must refresh against the new data.
This step can be time consuming. If the Model is going through a lot of changes
in a very short amount of time, shorter than the time needed to refresh the View, we might not want the View to follow through. This mechanism is known as "debouncing".

We can neutralize these fast changes in the Model either View-side or Model-side. 


# Design

The Model holds a timer. Every time a change is performed on the Model and the Timer is not running, the Timer is started. No notification is issued to the View until the Timer runs out.

<p align="center">
    <img src="images/delayed_model/delayed_model.png">
</p>

Being the timer asynchronous, particular care must be taken to guarantee that the event is not delivered when the Model is undergoing another change.

In both cases, if the new change overlaps with the previous one, the old change
can be discarded (as it will never get to appear on the view). Otherwise, the two changes can be combined
if the notification is qualified. If it's not qualified, then when the View is finally notified
at the end of the timer, it will get the current state.



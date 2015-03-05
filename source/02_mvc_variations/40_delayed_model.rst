Delayed model
-------------

To neutralize fast changes in the model that would hog the View with notifications

It can do this with a timer. When a change is detected, the model has a timer that is started.
If a new event needs to be delivered before the timer is expired, it can either reset the timer, or
keep the timer as is. In both cases, if the new change overlaps with the previous one, the old change
can be discarded (as it will never get to appear on the view). Otherwise, the two changes can be combined
if the notification is qualified. If it's not qualified, then when the View is finally notified
at the end of the timer, it will get the current state.



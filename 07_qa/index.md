Questions and Answers, Tips and Tricks
--------------------------------------

In this chapter, I want to provide a collections of minimalistic "good ideas" when dealing with MVC.
These suggestions didn't fit well with the overall presentation given in the previous chapters, yet
they are apparently trivial observations that can have an impact on the implementation correctness,
readability, and performance.


**Should I use a simple container approach (e.g. key/value dictionary with notifications) as a model, instead of a full-fledged object?**

A simple container like a key/value dictionary can technically be used as a
   model, often enriched with notification features. Typically, these Models
    have an agreed convention on the key, normally a string.
    This solution is fine for trivial Models, but as the amount of stored data grows,
    its unstructured nature and mode of access will lead to entangled, inconsistent 
    and undocumented storage. The model will be a “big bag of data” with very
    little clarity or enforced consistency.

    Enforcing access through well defined object relations and interfaces is
    recommended for models beyond the most trivial cases. 


**How to report errors in the View?**

    This is more of a Human Interface design question, but the choice can influence the
    design choices at the level of Model and View. It also depends on the data. Individual
    values that are incorrect can be marked in red. Typically, the user would input some data.
    the value would be checked for validity, and if found invalid, the View would be changed
    to express this information. This case probably enjoys using a Local Model, so that changes
    can be discarded and the original Model is left untouched. It also means that the Model
    must be able to accept and preserve invalid data, because this invalid data
    may be a step stone to reach a correct state after additional modifications.


**Updating an invisible View**

    When the view is shown, it will have to update its content. However, if the
    view is not visible, we have two choices:
      - either it should not receive events at all, by unsubscribing from 
        the Model when hidden
      - or it should keep receiving events, but simply discard any further processing
        if not visible.

    The need for this consideration relies on the graphical toolkit used, and the kind of processing
    encountered when the notification is delivered to the View. If the View
    requires time to refresh itself even when invisible, performance will suffer, and proper measures
    must be taken.

**Should the notification be sent before or after performing the change?**

It depends. Sending the notification before, and passing the new value, allows the View to obtain the
old value from the model, and the new value from the notification parameters.
Sending the notification after, the model retrieves the new value, and can get 
the old value carried by the notification. In some extreme cases, one can send
two notifications "aboutToChange" before, and "changed" after.
In the end, the answer to this question depends on the specifics of the
task. The required notification protocol will emerge from it.

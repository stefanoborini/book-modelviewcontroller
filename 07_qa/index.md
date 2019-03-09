---
nav_order: 7
has_children: true
---
Questions and Answers, Tips and Tricks
--------------------------------------

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



Local Model
-----------


**Addressed Need: Preserve the original Model's state so that changes can be reverted.**

This situation normally occurs when a View must modify a Model, but the View presents
the option to Cancel the changes. To achieve this functionality, the Model is first
copied. The View now observes the copied Model, and any changes occur on the copy.
This guarantees business rules are observed while changes are made on the data.

When the user clicks on the "Apply" button, the Controller submits the local copy to the
original Model, which is then in charge of performing the merge, and report notifications
for any data that may have changed. The Controller can also be in charge of this merging.
Optionally, the View can also have a "Revert" button which either performs a merge in
the opposite direction (original onto local) or simply discards the local
model, creates a new copy, and sets the View to the new copy.

If the user clicks "Cancel", the local model is simply discarded. 


Synchronization of view state
-----------------------------

in some cases, we have the following scenario. The View retains more state than the
model. If the model changes, and the view just fetches the new model data and repopulates itself,
the view will lose its state. This can be an annoyance.

An example is given by a View displaying a file tree, with the model providing filesystem data.
The view holds state in the form of opened/closed tree branches, or the position along the
scrolling area.

If a new file is added, the model will report a change has occurred, triggering a View actions.
A naive solution of purging and updating the content will have poor usability
consequences: the view will remove all its content, and reinsert the new data from the model.
This is unacceptable not only for performance reasons (although good caching may solve it),
but also because the View state will be discarded. Opened tree branches will be reset, and
the scrollbar will reset. Additionally, some flickering may appear of the View deleting
all its entries and repopulating itself again.



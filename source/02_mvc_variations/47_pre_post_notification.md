Pre/Post notification
---------------------

Two notifications: before changing the data, and after changing the data.
Useful for vetoing?

pre-notifications useful in keeping selection model synchronized.
When the model declares "about to remove lines", the selection model
receives this, and performs a removal of the selection (deselect the items).
This triggers a request for refresh from the View (selectionChanged) which is handled.
The data model hasn't changed yet, so the view is fetching valid data.

After this refresh is completed, the code in the data model continues and performs the
actual removal, again triggering the View for a refresh. An efficient graphic handling system
will pack these two changes into a single redraw, but the important point is that the data
is consistent along all the operation.


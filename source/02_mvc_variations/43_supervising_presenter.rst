Supervising presenter
---------------------

Supervising presenter is a simple partition of the Smart UI into logic and state classes.
All state stays in the View, and all logic stays in the Supervising Presenter. 
The presenter observes the View for notification of GUI events, and updates the View
through direct call. The View stays oblivious of the presenter, and acts therefore
as a passive view. Testing is simplified because the View can be replaced with a mock.

The state remaining in the view is visual state. The supervising presenter extracts only visual logic.

FIXME integrate this pattern into the others, as it's clearly a duplication and can be rendered as part of Passive View or MVP.


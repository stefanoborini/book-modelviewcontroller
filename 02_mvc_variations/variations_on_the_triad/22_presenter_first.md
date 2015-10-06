# Presenter First

More than a design, **Presenter First** is a discipline for coding a Dolphin
MVP. As briefly stated in the closing remarks of the previous section, it is possible
to deploy a Dolphin MVP variation where the View is fully passive.  

The presenter performs calls on both the model and the new, and receives events from
either of them.

Presenter First takes advantage of this choice to focus on the Presenter as the
starting point for development of a specific triad. The idea is that, by
creating the Presenter under direction of the customer's desires, there's a
chance to progressively discover the required interfaces of both the View and
the Model by coding against mocks and lastly implementing the discovered
interfaces.

The point of presenter first is to code the presenter to satisfy customer needs,
and code against it first. While the model provides a functionality and data oriented
access, the presenter describes the actions in terms the user understands or specifies.
The presenter has no state. It relies on the view and on the model to hold state, performing 
operations on these two. In principle, the Presenter should listen to events
from either the model or the view, meaning that it should not need public methods.
All the connections between events and presenter methods are setup by the presenter itself.


The Presenter should be tested strenously. The View, being a Humble View, can
be left untested.

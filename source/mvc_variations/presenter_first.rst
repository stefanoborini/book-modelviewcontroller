Presenter First
---------------

More than a design, **Presenter First** is a discipline for coding a Dolphin
MVP. As briefly stated in the closing remarks of the previous section, it is possible
to deploy a Dolphin MVP variation where the View is fully passive.  Presenter
First takes advantage of this choice to focus on the Presenter as the starting
point for development of a specific triad. The idea is that, by creating the
Presenter under direction of the customer's desires, there's a chance to
progressively discover the required interfaces of both the View and the Model
by coding against mocks and lastly implementing the discovered interfaces.

The Presenter should be tested strenously. The View, being a Humble View, can
be left untested.

Notification granularity
------------------------

notifications can have different levels of granularity. The coarse level is that the model reports
it changed, and let the View synchronize against the new data. Simple, but can become a bottleneck if
the redraw is forced even when data that are not displayed are modified. Also, the model gives no information
about what changed, which means that the view must either throw its whole state away and reset it anew,
or do a proper merge of all the data involved. This may create problems when visual state may be lost
(e.g. if an entry is open or close in a tree view)

a fine grained mechanism, where individual properties report their change.
(e.g. bound properties in javabean) Problem when multiple
properties must be changed in sequence, as they would trigger multiple useless
notifications. 

a qualified notification mechanism that gives details of the changeset.

Problem with double notification if one notification is a subset of another.
e.g. contentChanged/lineMetaChanged and contentChanged/lineAdded. How to handle
the double notification? Pass an "event id" in the signal so that the client 
realizes that it's the same change that delivers two messages?


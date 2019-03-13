---
grand_parent: 2 MVC Variations
parent: 2.5 Variations on the triad
nav_order: 9
---
# 2.5.9 Presenter-Adapter-View

Sometimes, in the management of the visual aspect of the view, it pays off to extract some of
the code of the presenter and isolate it into a separate adapter object. This adapter
object encapsulates the logic for some visual representation. The presenter,
instead of talking directly to the View, talks to the Adapter that transforms this
request into a proper rendering on the view.

For example, if we want to color a label red when a value is too high, the presenter
can use an adapter where the logic for setting something to red is according to the value.
the presenter sets the value on the adapter, which in turns sets the value on the view
and changes the color of the label appropriately.

The adapter needs not to know the business rules. The adapter can query the model
to ask if a given value is above or below a certain range, and choose the color appropriately.

Once again, the adaptor is simple to test.

In addition, one can extract an "adapter model" and have the presenter push data into the adapter
model. The adapter then takes these data, and push them to the specific part of the view.


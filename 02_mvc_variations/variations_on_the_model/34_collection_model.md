# Collection Model

A collection model is similar to the compositing model, with the only
difference that its role is to hold instances of a specific model class.
A sample implementation can be found in BackboneJs Collection.

The Collection Model is designed to emit a changed event when any of its
contained instances change, and also emit events when a new item is added
or removed.


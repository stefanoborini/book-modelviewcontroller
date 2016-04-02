# Pre/Post notification

### Motivation

The Model wants to inform its listeners not only when data have been changed,
but also just before changing them. A common reason behind this need is to support
vetoing, but other motivations may exist.

### Design

To implement Pre/Post notification, the Model simply issues two different
notifications, one before changing the Model state, and one after.
These notifications must be qualified, otherwise the interested listeners
would not be able to differentiate the pre-vs-post nature of the received 
notification.  For example, a Model could issue ``about_to_change``, apply the
change, and finally issue ``changed``.  Both the old and new value are also
generally passed as part of the notification.

### Practical Example

Although other implementation approaches could be used to handle this specific
need, pre-notifications can be useful in keeping a Selection Model synchronized
when the View in not collaborative in handling 

Our example has a Model containing a list of items, and a Selection Model 
holding information about which items in the Domain Model are selected. 
We assume that the View is unable to handle entries in the Selection Model 
that are not present in the Domain Model. Due to this implementation detail,
the following scenario would break the View:

1. An item in the Domain Model is currently selected. This implies that an entry 
   for this item is present in the Selection Model.
2. A Controller issues a request to the Domain Model to remove the item.
3. The Domain Model removes the item, and notifies the View of its change.
4. The View renders the Domain Model, followed by rendering the Selection, but 
   the item is no longer in the Model. The View cannot handle this situation and
   issues an exception.

Using a pre-notification can work around the View implementation detail:

1. A Controller issues a request to the Domain Model to remove the item.
2. The Domain Model issues an "about to remove item" pre-notification.
3. The Selection Model listens and receives the Domain Model pre-notification.
4. The Selection Model reacts by removing the item from its internal state.
5. The Selection Model change triggers a notification to the View which is handled
   by visually deselecting the item. The Domain Model hasn't changed yet, so the 
   View is retrieving valid data.
6. Finally, the Domain Model removes the item, and post-notifies the View to 
   re-render itself with one less item.

Through pre-notification, the View retrives consistent data throughout the operation.



---
parent: Variations on the notification strategy
---
# Qualified Notification with Subscribing

### Motivation

In this variation of Qualified Notification, the listener specifies which change
it is interested in, and a notification is issued only with the relevant change
occurs. The two solutions therefore differ in which entity performs filtering
of unnecessary notifications: in Qualified Notification the filtering is performed
by the listener, after the notification is delivered, while in Qualified
Notification with Subscribing, the filtering is performed by the Model,
honoring the listener's registration instructions.

### Design

For a Qualified Notification with Subscribing, the Model must support:

- an appropriate signature for the `register()` method, allowing to specify the type
of modification a listener is interested in.
- preservation of the passed information in an internal registry, which will be
  used during notification.

When the Model experiences a change in its content, it must consult its
internal registry to verify if a listener is interested in this information.
The Model then informs the listener only if this is the case.

### Practical Example: Apple KVO (Key-Value Observer)

Apple KVO (Key-Value Observer) is a form of Qualified Notification with Subscribing.
The Model supports an `addObserver` method, whose signature allows to specify  
the property the listener is interested in, and the type of change. For example, a 
listener registers for changes on the Model property `my_property` with the following call 

```objective-c
[model addObserver:destination
       forKeyPath:@"my_property"
       options:NSKeyValueChangeNewKey
       context:nil];
```

When the `my_property` value changes, the listener's method
`observeValueForKeyPath:ofObject:change:context:` will be invoked on the
listener. Changes in other Model's properties will not be delivered.

### References

- [Key-Value Observing Programming Guide](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html)
- [KVO considered harmful](http://khanlou.com/2013/12/kvo-considered-harmful/)


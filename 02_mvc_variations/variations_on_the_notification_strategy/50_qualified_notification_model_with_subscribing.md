# Qualified Notification with Subscribing

### Motivation

In this variation of the Qualified Notification, the View registers as a listener
to the Model specifying which changes is interested in. A notification is issued
only with the relevant change occurs.

### Design

the View register itself and lists which messages it is interested in.
Only if this matches, the message is delivered. 

can't a view fetch information from multiple models, and deliver signals to different controllers having different roles?

A View can depend on different Models, but this requires the View to know which
Model is delivering the notification.  Add a note on the fact that if the model
pushes information, then this
information characteristics falls on the signature of the notifyObserver()
methods. So, its signature must be somehow generic. The model pretends to know
what the view is specifically interested in, something it might not know, so it
must simply send itself, and let the view go through it, or have a protocol to
specify what changed.

The view does not inquire the model through an interface.
The model is closed to that. it just produces events with
a data change object, and synchronizes through that.


### Practical Example: Apple KVO (Key-Value Observer)

Apple KVO A form of qualified notification where every change in property of an object
is delivered to its listeners with the qualification of the name of
the changed property, and the object whose property changed. The listener
receives this notification through a single method.

The Model object supports an `addObserver` method. Differently from a traditional
MVC registration method, it is possible to specify the specific property
the listener is interested in. The listener will register for changes on
the Model property `my_property` with the following call 

```
[model addObserver:destination
       forKeyPath:@"my_property"
       options:NSKeyValueChangeNewKey
       context:nil];
```

will add an observer to the "source" object so that it will send an observeValueForKeyPath:ofObject:change:context: message to destination every time the setMyValue: method is invoked.

All you need to do is have every listener register themselves with the observee and have the listeners implement observeValueForKeyPath:ofObject:change:context:.

Used in Apple Cocoa. Main problem is that the qualification model now requires to
check the changed property against a string, which is prone to typos.

### References

- [Key-Value Observing Programming Guide](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html)
- [KVO considered harmful](http://khanlou.com/2013/12/kvo-considered-harmful/)


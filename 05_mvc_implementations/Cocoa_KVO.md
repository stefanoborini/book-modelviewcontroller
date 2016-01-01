# Key Value Observer

### Motivation

A form of qualified notification where every change in property of an object
is delivered to its listeners with the qualification of the name of
the changed property, and the object whose property changed. The listener
receives this notification through a single method.


### Design

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

### Practical Example

Used in Apple Cocoa. Main problem is that the qualification model now requires to
check the changed property against a string, which is prone to typos.

### References

- [Key-Value Observing Programming Guide](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html)
- [KVO considered harmful](http://khanlou.com/2013/12/kvo-considered-harmful/)

Model-View-ViewModel (Model-View-Binder)
----------------------------------------

**Addressed Need:**

The MVVM is a specialization of the Presentation Model. It is rather popular in
the Windows world, particularly WPF and Silverlight.

MVVM has a traditional model, an active view (generally declared as a XAML
description) that handles its own events internally and acts both on the Model
and the ViewModel. The View and the ViewModel contents are bound together in a
direct simple relationship through bindings. A checkbox on the view can be
bound to a boolean field in the ViewModel. In other words, the ViewModel is the
“Model of the View” intended for the representation the view has of the data.
The Model, in fact, might contain a different representation of the values (for
example, in the Model vision of things, that checkbox could represent the
existence of a reference between two Model objects). The ViewModel is
responsible of mapping its state (the boolean) to setting the reference, and
vice-versa.

Similar to Presentation Model/Application Model, however, the ViewModel has
no explicit reference to the View, nor explicit code to direct the View. 
Instead, it uses data binding, which offloads the sync task from the developer.



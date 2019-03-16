---
grand_parent: 1 Basics of MVC
parent: 1.4 In depth analysis of MVC roles
nav_order: 1
---

# 1.4.1 The Model

Entities taking the Model role are responsible for holding the running state
and business functionality of the application, either as a whole or as the part
that is relevant to that specific MVC Triad, as either data (stored values) or
activity (routines computing relevant data). They define the protagonists of
the application's domain, their mechanism of operation and cooperation. Model
objects can represent, for example, 

   - An interface to a database, filesystem, low level driver, hardware machine
   - Access to a computational backend.
   - Proxies for a remote service 
   - A representation of business entities such as weather forecast in a
     specific area, people's details in a phonebook, tracks information in a
     music CD, student grades
   - In some designs, information related to the GUI, such as selected items, or
     the X-axis scale of a plot. 
   - A running process.

When implemented, a Model can go from a dictionary-like of key/value pairs to a
complex network of objects with well defined interfaces. Regardless of the
implementation, Models must provide the following three services: 

**Querying**: to inquire about their current state, either represented by
high-level domain objects (Object Oriented approach), or through an IO
layer of routines providing access to the data (Data Oriented approach). In the
Object Oriented approach, the Model objects generally represents an
identifiable part of the domain of your application, and provide access to data
through a well-defined object-oriented interface. The Model can also perform
computation, generally of information derived or associated to the main data it
represents. In the Data Oriented approach, the routines “speak the domain
language” and have high-level semantics to access the data, generally from a
data storage (e.g. disk).

**Altering**: to modify the current state. The Model interface provides setter
methods or routines to modify its state. The Model performs consistency
checks about the data it handles, enforcing fundamental integrity: for example,
it can raise an exception or ignore the passed data if a method
``set_current_temperature`` is called passing a string instead of a float, or a
method ``set_length`` is called with a negative value. 

**Notifying**: to inform interested parties that a change has occurred in its
state. The Model allows interested objects to listen for change notifications. 
When a change occurs, these objects will be notified of this
fact and can act accordingly, normally by synchronizing themselves against the
Model's new contents. 

Model objects should provide core application functionality through a clear and
self-documenting interface, exposing what can be done with the program's state.
To operate, they can depend only on other Model objects or other components of
the application that don't involve presentation, like an IO or Service layer. 
The relationship among Model objects is that of a **strong dependency**.  

On the other hand, a Model should not contain nor be dependent for its
functionality on any graphical entity, nor contain formatting/visual logic for
presentation (*e.g.* logic to make a negative value represented in red, or logic
to present the date in US vs. ISO representation). Model objects should be
completely unaware of how user interaction is handled by the application they
live in, and should have a **weak dependency** toward its listeners via the
notification generic interface. 

For data modification, all the Model does is to process incoming requests in
the form of method calls.  Normally these requests are performed by
Controllers, but a Model can also change due to requests from other subsystems
(for example, a subprocess executing in the background), from another Model 
component or because it is monitoring a backend (e.g. a database, or a filesystem) 
and the monitored entity changes. The only entities never allowed to issue a 
change request to the Model are the Views. 

The Model should enforce **integrity** of the data, but it does not necessarily
enforce **validity**: data might be correct (for example, integers for min/max
values) but overall invalid for computation (for example, if min > max). While
integrity should be enforced, storing invalid data can be acceptable: depending
on the application, invalid data may be marked as such in the Model by the part
of the code that detects the invalidity, so that the View can represent it (for
example, with a red font); An invalid state might be needed as a stepstone to
reach a valid state at the end of a set of changes done by the User via the UI.

With the above guidelines and restrictions in place, the resulting
implementation is robust, flexible and testable: Views and Controllers are the
components that change the most as the application evolves, and a Model that is
agnostic to these changes is easier to code and maintain. The Model can be
tested independently from the rest of the application, and it opens itself to
scripting, allowing the User to change the Model programmatically instead of
through the GUI. 


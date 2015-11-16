# Supervising Controller

### Motivation

Toolkits and UI frameworks can provide declarative generation of a View with
direct binding (see Variations on the Triad: Data Binding) between data 
in the Model and a corresponding Widget in the generated View. This declarative 
approach can simplify the deployment of a View, but can be of limited expressive power.

Supervising Controller complements the declarative View to address complex logic that
the View is unable to handle.

### Design

The overall design has two channels for modifying the View:
- The first channel connects the Model to the View through declarative Data Binding. When a specific property in the Model changes, the declared associated View's Widget is updated to the new value. 
- The second channel handles those modifications that cannot be handled 
easily by this mechanism. For example, the Supervising Controller receives the notification of the property change from the Model, and acts on the View to change the background color of the Widget, for example to report an incorrect value.

The Controller channel thus enhances the Data Binding channel by acting on the View.
The same mechanism handles the opposite communication route (View to Model): direct Data Binding handle transporting simple data from the View's widgets to the associated Model's properties, but more complex events, or events requiring complex Model transformations, or events that are not mappable to a Model property (like, for example, a button press) are handled by the Supervising Controller.



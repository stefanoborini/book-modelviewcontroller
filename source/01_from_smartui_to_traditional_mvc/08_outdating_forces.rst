Forces outdating Traditional MVC
================================

Traditional MVC is an old approach. Much has changed since its original
implementation.  For example, modern Views are composed of widget that handle
events internally: a Line Edit widget receives and handles keyboard events independently,
and can transform these events in an internally handled operations to actually write text
on the screen, without any additional help. Moreover, a modern View is
generally able to keep track of which Controller to send notifications to, by
having hints about their focus status. In the past, this coordination was
performed by the Controllers, who had to be connected and forward messages
to each other to decide who was in charge of handling a specific event.

The result of a more integrated and effective handling of events decreased the
responsibility of the Controller. Now, the controller handles "events" from the view,
rather than raw, low level events. New interpretations of the old pattern emerged,
but there's definitely less pressure on the Traditional MVC Controller today as
there was once. 

Additionally, new needs emerged from more complex and communicative GUIs,
making Traditional MVC either too inflexible, or too limited to address these
requirements. 

off-the-shelf widget sets. Reimplement widgets to define methods for events is annoying. proliferates classes.

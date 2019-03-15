---
parent: 1 Basics of MVC
nav_order: 5
summary: How traditional explicit decomposition may be outdated by modern design
---
# 1.5 Forces outdating Traditional MVC

The Traditional MVC design presented in the previous section is a modern
reinterpretation of the MVC as described by Reenskaug in the 70s. The original
design was developed under different constraints, and could not take advantage
of the modern solutions we enjoy today. 

For example, Reenskaug's Controller handled low level events, positioned the
Views on the screen, and kept track of which View had focus and which
Controller in the application was in charge of handling the events. 

Modern environments, compared to the ones where Reenskaug MVC was developed
first, have improved on a lot of boilerplate tasks: modern Views are composed
of widgets provided by either a GUI Toolkit or the operating system's
framework. These widgets acts both as Views and as Controllers as originally
defined, because they can display and position themselves, manage focus,
receive low-level events and convert them to higher level behavior: a modern
LineEdit widget handles keyboard input to write text on the screen without any
additional support. An application-level event loop handles events and dispatches
them to the appropriate receiver.

The result of this modernization is a reduction of responsibility of the
Controller, and its role has been adapted with the times.  New interpretations
of the old pattern emerged, and the Traditional MVC introduced earlier is an
example of this adaptation.  The Controller now handles high-level events from
the View, rather than raw, low level events, and can eventually take the role
of mutator of the Model.

On the other hand, new needs emerged from more complex and communicative GUIs,
underlying toolkits, and new architectures (i.e. the web) making Traditional
MVC sometimes too inflexible, sometimes too limited, and sometimes overdesigned
for the specific task at hand.

In the next chapter, we will examine a palette of variations of the basic
building blocks of MVC to provide development strategies for common GUI
development needs.

FIXME:
off-the-shelf widget sets. Reimplement widgets to define methods for events is annoying. proliferates classes.
Controller was in charge of deciding when to relinquish control to other controllers.
The active controller was the one handling events.
Modern widgets handle damage control (e.g. due to hiding/showing) by themselves. The view
is only left the task of updating against a modified model. The toolkit takes care of
keeping the visual correct.

Explain widget as a UI element which has no connection to a model.

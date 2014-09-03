Dolphin Model-View-Presenter
----------------------------

**Additional Need: Rationalize Application model into a more active role**

The Dolphin Model-View-Presenter (MVP) schema is an evolution of 
the Application Model approach. Although it is derived from the Taligent/IBM
strategy with the same name, we will examine Dolphin first as it is simpler to
describe within the concepts we already introduced. The Dolphin strategy is
also the one most often referred as "Model View Presenter" without additional
clarification. To add to the nomenclature, Fowler identifies the Presenter
with the more appropriate "Supervising Controller".

As we introduced in the Application Model section, the main purpose of this
Model is to hold visual state, acting as an intermediate between the Domain
Model and the View/Controller pair. The Application Model was a model in every
respect in terms of design: it performs notifications, remains oblivious of
its listeners, is directly accessed by the View and modified by the Controller.
Yet, due to the strictly specific nature of the visual state, it would be
convenient if the Application Model could handle visual logic and refer to the
View directly, like the Controller does, while still keeping and handling View
state.

Let's analyze the Controller: with widgets of modern GUI toolkits handling
low-level events (e.g. physical keyboard presses), the controller has only the
duty of modifying the models according to higher level events (e.g. textlabel
content modified). These events are then transformed by Controller logic in
actual Model changes, some of which may have an impact on the visual state,
which is stored in the Application Model. It seems like a good idea to have an
Application Model containing this visual state if the assumption is that this
state (e.g. a field being red) is shared among Views. Once again, this state
is almost never shared and mostly tied to a specific View.

Summing up, the roundabout mechanism the Controller uses to take care
of purely visual state would be considerably simplified if we define
a new role, the **Presenter**, which combines the Application Model and the 
Controller in a single entity. 

Like the Application Model, the Presenter:
    
    - holds visual state, and keeps it synchronized against changes in the
      Domain Model
    - converts business rules (e.g. engine rpm number too high)
      into visual representation (e.g. label becomes red)
    - eventually handles state for selection, and application of actions
      to the subset of the Model specified by this selection.

and like the Controller, the Presenter:

    - it is tightly coupled to the View.
    - refers to the View directly, and can act on it to alter its 
      visual aspect.
    - handles View events, converting them into action through proper logic.
    - modifies the Domain Model, which contains no visual state
    - handles View logic according to the View state it contains

The Domain Model is unchanged, and is still accessed by the View for data
extraction and from the Presenter for data modification. The View 
fetches data directly from the Domain Model, instead of having to rely
on the Application Model as a forwarder. The View behavior is now hybrid
Active/Passive, fetching Domain data directly from the Domain Model but with
visual aspects applied by the Presenter (Passive). A variant with a fully
Passive View is possible.

FIXME: Add Picture
FIXME: reformulate in general


Humble Dialog
-------------
With the Humble dialog approach, the View is passive, and its contents is set
from the outside by a ControllerModel object. Widgets in the View have no
awareness of the Model. This approach reduces as much as possible the code that
is hard to test (Graphical interaction) to an extremely thin layer of
one-to-one Model-View connections that act on the widgets.  The diffeernce with
PassiveView is that in passive view the widgets are under direct control of the
controller. in Humble dialog they are bound 



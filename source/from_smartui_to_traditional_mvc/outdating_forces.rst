Forces outdating Traditional MVC
================================

Traditional MVC is an old approach. Much has changed since its original implementation.

Modern Views keep track of which controller to send notifications to. In the past,
this coordination was performed by the Controllers, who had to be connected and forward messages
among each other to decide who was in charge of handling a specific event.


MVC Variation
=============

Traditional MVC is excellent as a starting point for discussion, but by no
means it must be considered the one and only proper way of doing MVC: real
applications are built around its basic concepts, but include plenty of tricks,
extensions and alternative design choices to satisfy the final requirements
while keeping programming complexity as low as possible. Examples of such
requirements include:

   - a modal dialog must allow changing values, but revert them when the Cancel
     button is pressed.
   - a modeless dialog allows changing values while the change is visible in
     another window, but must be reverted if “Restore” is pressed.
   - prevent typing of invalid values, for example a string in a line edit
     supposed to accept only digits will not accept any key presses from
     non-digits.
   - alternatively, allow invalid entries, but disable the Ok button and mark
     the incorrect value red.
   - and so on...

As you can see, the complexity of an application made of hundreds of menus,
text input areas and buttons, plus all the possible logical dependencies among
them can grow considerably. Unexpected interactions and strange communication
patterns emerge in the form of bugs or application freezes. Keeping this
communication network well organized and confined by enforcing a structure is
of paramount importance.

In this chapter we will examine alternative design in MVC able to deal with
more complex use-case scenarios, constrained by requirements, architectural
needs or self-documentation purposes.

.. toctree::
   :maxdepth: 2

   compositing_model
   model_pipe_view_controller
   application_model
   side_by_side_application_model
   qualified_notification_model
   passive_model
   model_controller
   model_view_adapter
   model_gui_mediator
   local_model
   value_model
   model_view_notification_decoupling
   application_controller
   passive_view
   widget_level_container_level
   push_vs_pull
   reenskaug_mvc
   dolphin_mvp
   presenter_first
   taligent_mvp
   model_view_viewmodel
   view_controller_view
   visual_proxy
   notification_looping_prevention
   commands
   data_dialog



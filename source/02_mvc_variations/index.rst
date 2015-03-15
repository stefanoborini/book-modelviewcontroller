MVC Variation
=============

Traditional MVC is excellent as a starting point for discussion, but by no
means it must be considered the one and only proper way of doing MVC. In fact,
MVC is rather limited within the context of modern UI development. New patterns
have emerged, built around MVC basic concepts but with additional tricks,
extensions and alternative design choices to satisfy modern requirements while
keeping programming complexity as low as possible. Examples of such
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

Design aims at managing complexity. The MVC details given in this book are
guidelines, but need to consider the actual real problem at hand. Some
flexibility is needed. Strict compliance generally produces a benefit, and has
better communicative consistency within the development team, but may not scale
up to specific cases. In that case, reconsider the design, or relax some
constraints, but aim at keeping logic encapsulated and object interaction
simple and straightforward.

In this chapter we will examine alternative design in MVC able to deal with
more complex use-case scenarios, constrained by requirements, architectural
needs or self-documentation purposes.

Variations on the Model
~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 1

   01_compositing_model
   02_model_pipe
   03_application_model
   04_side_by_side_application_model
   05_qualified_notification_model
   06_ui_retrieving_model
   07_passive_model
   08_lazy_model
   09_model_controller
   12_local_model
   13_value_model
   32_proxy_model
   34_collection_model
   35_accumulator
   38_view_aware_model
   40_delayed_model
   42_caching_model
   47_pre_post_notification
   48_vetoers

Variations on the View
~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 1

   14_mvc_pluggable_view
   17_passive_view
   18_widget_level_container_level
   27_visual_proxy
   30_data_dialog
   41_visibility_allowed_notifications
   46_synchronization_view_state

Variations on the Controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 1

   39_supervising_controller

Variations on the Triad
~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 1

   10_model_view_adapter
   11_model_gui_mediator
   15_model_view_notification_decoupling
   16_application_controller
   19_push_vs_pull
   20_reenskaug_mvc
   21_dolphin_mvp
   22_presenter_first
   23_taligent_mvp
   24_presenter_adapter_view
   25_model_view_viewmodel
   26_view_controller_view
   28_notification_looping_prevention
   29_commands
   31_model_delegate
   33_event_filter
   36_visual_editor
   37_command_notification
   45_Qt_MVC



FIXME:
off-the-shelf widget sets. Reimplement widgets to define methods for events is annoying. proliferates classes.



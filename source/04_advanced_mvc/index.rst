Advanced MVC
============

Event bus / PubSub
------------------

Example, wxpython provides a nice example of pubsub model

.. code::

    import wx
    from wx.lib.pubsub import Publisher

    class Model:
        def __init__(self):
            self.myMoney = 0

        def addMoney(self, value):
            self.myMoney += value
            Publisher.sendMessage("MONEY CHANGED", self.myMoney)



The controller can now subscribe to the qualified notification as follows. The 
handler will receive a message, qualified with the appropriate information

.. code::

    class Controller:
        def __init__(self, app):
            # <...>
            pub.subscribe(self.moneyChangedHandler, "MONEY CHANGED")

        def moneyChangedHandler(self, message):
            """
            This method is the handler for "MONEY CHANGED" messages,
            which pubsub will call as messages are sent from the model.

            We already know the topic is "MONEY CHANGED", but if we
            didn't, message.topic would tell us.
            """
            self.view.setMoney(message.data)


An additional flexibility of this mechanism, compared to the pubsub mechanism
proposed earlier, is that messages can now be spooled, packed, and delivered
asynchronously, if the need emerges.

For example, a message producer occasionally producing bursts of changes
could put the notification in a spool. When the spool delivers the messages
it can verify that actually multiple notations have been performed within 
a small amount of time, and simply deliver to the listener only one message,
removing trashing caused by excessive refresh requests.


Vetoing the changes
-------------------

Some interface design may require vetoing of a specific change on the Model.
Vetoers are specific listeners to the model. When the model is requested to change
a value, it issues an aboutToChange() notification, passing the new intended
value. This event is reported to the listeners which evaluate the proposed
change and respond with an ok/not ok state. As the model notifies all vetoers,
it collects the responses and aborts the change if one vetoer returns the
change as not ok. If all vetoers approve the change, then the change is
performed and the model issues a changed().

Model undoing changes
---------------------

An alternative to the command pattern and to the local model (copying the model
locally and modifying the local copy, then merging with the current model on "Apply")
Instead, the model can keep both the current data and the old data, and has a method
revert(). Revert restores the old data and synchronizes the views. the method apply instead
removes the old values and set them to none, thereby accepting the current new values.

Model distribution
-------------------

Scriptability
Modification of the model programmatically can enable scripting

.. toctree::
   :maxdepth: 2

   model_persistence
   signal_object
   mvc_testing





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
   mvc_testing
   notification_granularity




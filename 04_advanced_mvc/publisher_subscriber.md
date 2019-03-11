---
parent: Advanced MVC
---
# Event bus / PubSub

Full decoupling between publishers and subscribers. 
Publishers don't know about subscribers, and vice-versa.
Messages are sender to receiver. The receiver cannot "reply" to the sender.


Example, wxpython provides a nice example of pubsub model

```python
    import wx
    from wx.lib.pubsub import Publisher

    class Model:
        def __init__(self):
            self.myMoney = 0

        def addMoney(self, value):
            self.myMoney += value
            Publisher.sendMessage("MONEY CHANGED", self.myMoney)
```

Objects that are interested in the notification can now subscribe to the 
qualified notification as follows. The 
handler will receive a message, qualified with the appropriate information

```python

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
```

NSNotificationCenter is a pubsub.

- decoupling makes compile time checks useless.
- delivery network can become complicated. Incorrect setup can lead to unintended listeners to receive
messages they are not supposed to receive.
the application flow is hard to understand and debug.
- from the code alone, it's hard to spot the dependency between a publisher and a subscriber,
in particularly when the message is emitted and delivered.
- delivery can be synchronous or asynchronous, but even when synchronous, it's not possible
to rely on delivery order.
- message source may not be available to the receiver.


use of topics to group message types.






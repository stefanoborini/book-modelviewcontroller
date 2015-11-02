# Event bus / PubSub

Full decoupling between publishers and subscribers.
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


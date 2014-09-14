#!/usr/bin/env python
# By Stefano Borini 2013. CC-SA

class BaseModel(object):
    def __init__(self):
        self._listeners = set()

    def register(self, listener):
        self._listeners.add(listener)
        listener.notify(self)

    def unregister(self, listener):
        self._listeners.remove(listener)

    def _notifyListeners(self):
        for l in self._listeners:
            l.notify(self)


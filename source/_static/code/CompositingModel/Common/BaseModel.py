#!/usr/bin/env python
# By Stefano Borini 2013. CC-SA

class BaseModel(object):
    def __init__(self):
        self._listeners = set()

    def register(self, listener):
        self._listeners.add(listener)
        listener.notify()

    def unregister(self, listener):
        self._listeners.remove(listener)

    def notifyListeners(self):
        for l in self._listeners:
            l.notify()


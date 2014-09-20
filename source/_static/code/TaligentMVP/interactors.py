#----------------------------------------------------------------------------
# Name:         interactors.py
# Purpose:      Event Management
#
# Author:       Peter Damoc (peter at sigmacore.net)
#
# Created:      January 2006
# Version:      0.2
# Licence:      wxWindows license

import wx

class AlbumInteractor(object):
    '''
    This class translates the low level events into the "higher level language" of the presenter
    '''
    def Install(self, presenter, view):
        self.presenter = presenter
        self.view = view
        view.albums.Bind(wx.EVT_LISTBOX, self.OnReloadNeeded)
        view.title.Bind(wx.EVT_TEXT, self.OnDataFieldUpdated)
        view.artist.Bind(wx.EVT_TEXT, self.OnDataFieldUpdated)
        view.composer.Bind(wx.EVT_TEXT, self.OnDataFieldUpdated)
        view.classical.Bind(wx.EVT_CHECKBOX, self.OnDataFieldUpdated)
        view.apply.Bind(wx.EVT_BUTTON, self.OnApply)
        view.cancel.Bind(wx.EVT_BUTTON, self.OnReloadNeeded)
        view.add.Bind(wx.EVT_BUTTON, self.OnAddNewAlbum)
        view.order.Bind(wx.EVT_BUTTON, self.OnToggleOrder)

    def OnAddNewAlbum(self, evt):
        self.presenter.addNewAlbum()

    def OnToggleOrder(self, evt):
        self.presenter.toggleOrder()

    def OnApply(self, evt):
        self.presenter.updateModel()

    def OnReloadNeeded(self, evt):
        self.presenter.loadViewFromModel()

    def OnDataFieldUpdated(self, evt):
        self.presenter.dataFieldUpdated()

# Author:       Peter Damoc (peter at sigmacore.net)
#               adapted from Martin Fowler's MVP example
# Created:      January 2006
# Version:      0.2
# Licence:      wxWindows license

import wx

class AlbumWindow(wx.Frame):
    '''
    This class holds the visual representation of your application
    '''
    def __init__(self):
        '''
        Here first we create the wx.App then we put together all the widgets
        '''
        self.app = wx.App(0)
        wx.Frame.__init__(self, None)
        self.SetBackgroundColour("lightgray")

        self.albums = wx.ListBox(self, size=(160, 240))
        self.artist = wx.TextCtrl(self, size=(160, -1))
        self.title = wx.TextCtrl(self)
        self.classical = wx.CheckBox(self, label="classical")
        self.composer = wx.TextCtrl(self)

        self.apply = wx.Button(self, label="Apply")
        self.cancel = wx.Button(self, label="Cancel")
        self.add = wx.Button(self, label="New Album")
        self.order = wx.Button(self, label="A->Z")

        leftSizer = wx.GridBagSizer(5,5)
        leftSizer.Add(self.albums, (0,0), (1,2),flag=wx.EXPAND)
        leftSizer.Add(self.add, (1,0), (1,1),flag=wx.EXPAND)
        leftSizer.Add(self.order, (1,1), (1,1),flag=wx.EXPAND)

        applyCancelSizer = wx.BoxSizer(wx.HORIZONTAL)
        applyCancelSizer.Add(self.apply, 0, wx.ALIGN_RIGHT)
        applyCancelSizer.Add(self.cancel, 0, wx.ALIGN_LEFT)

        albumSizer = wx.GridBagSizer(5,5)
        albumSizer.Add(wx.StaticText(self, label="Artist: "), (0,0), flag=wx.ALIGN_RIGHT)
        albumSizer.Add(self.artist, (0,1),flag=wx.EXPAND)
        albumSizer.Add(wx.StaticText(self, label="Album: "), (1,0), flag=wx.ALIGN_RIGHT)
        albumSizer.Add(self.title, (1,1), flag=wx.EXPAND)
        albumSizer.Add(self.classical, (2,0), (1,2), flag=wx.ALIGN_CENTER)
        albumSizer.Add(wx.StaticText(self, label="Composer: "), (3,0), flag=wx.ALIGN_RIGHT)
        albumSizer.Add(self.composer, (3,1), flag=wx.EXPAND)
        albumSizer.Add(applyCancelSizer, (5,0), (1,2), flag=wx.ALIGN_CENTER)


        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        mainSizer.Add(leftSizer, 0, wx.EXPAND|wx.ALL, 5)
        mainSizer.Add(albumSizer, 0, wx.EXPAND|wx.ALL, 5)

        self.SetSizerAndFit(mainSizer)

    def setTitle(self, title):
        self.title.SetValue(title)

    def setArtist(self, artist):
        self.artist.SetValue(artist)

    def setClassical(self, isClassical):
        self.classical.SetValue(isClassical)

    def setComposer(self, composer):
        self.composer.SetValue(composer)

    def setComposerEnabled(self, enabled):
        self.composer.Enable(enabled)

    def setApplyEnabled(self, enabled):
        self.apply.Enable(enabled)

    def setCancelEnabled(self, enabled):
        self.cancel.Enable(enabled)

    def setWindowTitle(self, title):
        self.SetTitle(title)

    def setAlbums(self, albums):
        '''
        This method contains a small optimisation to take care of the flicker that appears during
        the updates. Exercise: comment out the Freeze and Thaw lines and see what happens
        '''
        self.Freeze()
        self.albums.Set([album.title for album in albums])
        self.Thaw()

    def setSelectedAlbum(self, albumIndex):
        self.albums.SetSelection(albumIndex)

    def setOrderLabel(self, label):
        self.order.SetLabel(label)

    def getOrderLabel(self):
        return self.order.GetLabel()

    def getTitle(self):
        return self.title.GetValue()

    def getArtist(self):
        return self.artist.GetValue()

    def getComposer(self):
        return self.composer.GetValue()

    def getSelectedAlbum(self):
        return self.albums.GetSelection()

    def isClassical(self):
        return self.classical.GetValue()

    def start(self):
        '''
        Upon start we just show the frame and enter the MainLoop
        '''
        self.CenterOnScreen()
        self.Show()
        self.app.MainLoop()

#----------------------------------------------------------------------------
# Name:         mock_objects.py
# Purpose:      Mock objects to be used by the tests, as you can see... no wx
#
# Author:       Peter Damoc (peter at sigmacore.net)
#               adapted from Martin Fowler's MVP example
# Created:      January 2006
# Version:      0.2 
# Licence:      wxWindows license

class MockAlbumWindow(object):
    def __init__(self):
        '''
        Just a simple object to hold view status data
        Hint: if you have  setXXX in the original view you should have a field to hold that 
        '''
        self.title = ''
        self.artist = ''
        self.classical = False
        self.composer = ''
        self.composerIsEnabled = False
        self.apply = False
        self.cancel = False
        self.windowTitle = ''
        self.albums = []
        self.selected = -1
        self.orderLabel = ""
        
    def setTitle(self, title):
        self.title = title
        
    def setArtist(self, artist):
        self.artist = artist
        
    def setClassical(self, isClassical):
        self.classical = isClassical
        
    def setComposer(self, composer):
        self.composer = composer
        
    def setComposerEnabled(self, enabled):
        self.composerIsEnabled = enabled
        
    def setApplyEnabled(self, enabled):
        self.apply = enabled
        
    def setCancelEnabled(self, enabled):
        self.cancel = enabled
        
    def setWindowTitle(self, title):
        self.windowTitle = title
        
    def setAlbums(self, albums):
        self.albums = albums
        
    def setSelectedAlbum(self, albumIndex):
        self.albumIndex = albumIndex
        
    def setOrderLabel(self, label):
        self.orderLabel = label
        
    def getOrderLabel(self):
        return self.orderLabel
        
    def getTitle(self):
        return self.title
    
    def getArtist(self):
        return self.artist
        
    def getComposer(self):
        return self.composer

    def getSelectedAlbum(self):
        return self.albumIndex

    def isClassical(self):
        return self.classical

    def start(self):
        pass

class MockAlbumInteractor:
    def Install(self, presenter, view):
        pass
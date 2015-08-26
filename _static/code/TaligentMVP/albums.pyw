#!/bin/env python
#----------------------------------------------------------------------------
# Name:         albums.pyw
# Purpose:      starts everything
#
# Author:       Peter Damoc (peter at sigmacore.net)
#               adapted from Martin Fowler's MVP example
# Created:      January 2006
# Version:      0.1
# Licence:      wxWindows license

import presenters
import models
import views
import interactors

'''
Just creates the Presenter with some albums, a way to display them(the View)
and a way to interact with them (the Interactor)
'''
presenters.AlbumPresenter(models.GetDemoAlbums(), views.AlbumWindow(), interactors.AlbumInteractor())

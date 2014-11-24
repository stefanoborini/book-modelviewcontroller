UI Retrieving Model
-------------------

This small variation of the model is limited to very specific cases. One
important constraint about the model that we stressed throughout the book
is that it should never be involved in GUI related business. UI Retrieving
Model breaks this rule. Credit for this approach goes to Scott Miller.

The role of the Model is to retrieve information. In general, the backend
retrieval is performed from a file, memory, or a database. However, the Model
may be requested information that only a direct session with the user can
accomplish. In this case, the Model may pop up a GUI dialog to request the
information. In practice, the Model is considering the User as a database,
whose API involves the use of graphical widgets.

One trivial example of this pattern would be a Model object representing
the User session, with a password field initially set to null. When the
program starts the session, it will ask for the credentials to the Model layer.
Asking the username will return the proper string, but asking the password may
return null if no password has been set yet. The model is then authorized
to retrieve this information from the User by a GUI dialog, maybe trying
some non-interactive strategies first, like checking in a configuration file.
When the user acts on the dialog, the Model stores the password and returns
it to the Presenter layer, which then proceeds with the authentication logic.
If the password is incorrect, the presenter will ask the Model user to reset
the password field, and the user will be prompted again for the password, otherwise
any additional request will use the cached password without additional requests
to the user.


 

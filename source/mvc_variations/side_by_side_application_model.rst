Side-by-Side Application Model - Selection Model
------------------------------------------------

**Addressed Need: Keep View state in a separate Model, not wrapping the Domain Model.**

An alternative approach to Application Model is possible: instead of wrapping
the Domain model, the Application Model provides only visual state and
functionality. The View depends on both Models

[picture]

Obviously, the Application Model keeps registering itself on the Domain model::

   class DialViewModel(BaseModel):
      def __init__(self, engine):
      super(DialViewModel, self).__init__()
         self._dial_color = Qt.green
         self._engine = engine
         self._engine.register(self)

      def color(self):
         return self._dial_color
      
      def notify(self):
         if self._engine.isOverRpmLimit():
            self._dial_color = Qt.red
         else:
            self._dial_color = Qt.green
         self._notifyListeners()

The dial now registers to both Models, and listens to notifications from both.::

   class Dial(QtGui.QDial):
   <....>
      def setModels(self, model, view_model):
         if self._model:
            self._model.unregister(self)
         if self._view_model:
            self._view_model.unregister(self)

         self._model = model
         self._view_model = view_model

         self._controller.setModel(model)
         self._model.register(self)
         self._view_model.register(self)

      def notify(self):
         self.setValue(self._model.rpm())  
         palette = QtGui.QPalette() 
         palette.setColor(QtGui.Qpalette.Button,self._view_model.color())
         self.setPalette(palette)

Note how the Dial cannot differentiate which of the two Models is delivering
the message, and how in particular it will be potentially notified twice: once
by the change in the Domain model, and another time by the change in the
Application Model, in itself triggered by the previous change in the Domain
model. Particular care may be needed if the notify method is time consuming.
Another case of Application Model usage is a plot with changing scale. The
state of the View (its scale and positioning) is part of a “separate model”
that is pertinent only to the View. The Domain model, which holds the plot
data, should not be involved in the zoom factor or plot limits.

A side-by-side solution is frequently used to implement selection, a common GUI
paradigm to operate on a data subset. Selected data normally have a different
visual aspect, such as highlighting or a checkbox. This information is then
used to drive operations on the specified subset. Selection has therefore a
dualistic nature of holding state that is both visual and business related.  A
trivial strategy is to include selection state directly on the Domain Model,
for example as a flag associated to the item. Depending on the application,
this may or may not be an appropriate solution: if two Views observe the same
Model, and an item is selected in one View, you might or might not want the
other View to obtain this selection information. For example, a GUI allowing
the user to select elements from a list, but also have a label saying “3 items
selected” would work with selection on the Domain Model. If selection cannot be
shared between Views, or we want to keep selection as an independent concern,
a sensible strategy is to host it as a separate side-by-side Selection Model.

One problem with a Selection Model is that it must be tolerant to changes in
the Domain Model. If a selected entity is removed from the Domain Model, the
selection status must be cleared of that entity. This is important, because if
the Selection Model is then used to perform collective operations (for example,
change the color of all selected items) an operation will be attempted on an
item no-longer existing in the Domain Model. Add operations are also not immune
from problems: the Selection Model might have to resize itself to match the
Domain Model, so that it does not go out of bounds when inquire is performed
about the selection status of the new entries. Modifications may reorder and
invalidate indexes in the Domain Model, making the selection outdated. Finally,
when synchronization is achieved between the Domain Model and the Selection
Model, the View will be notified twice: once by the change in the Domain Model,
and again by the Selection Model. 

invert selection, complex selections, select all, select none.  If data is
added, removed, or modified in the model, the Selection Model must respond
accordingly. For example,


---
grand_parent: 1 Basics of MVC
parent: 1.4 In depth analysis of MVC roles
nav_order: 2
---
# 1.4.2 The View

We introduced the View as the component of our application whose role is to
interact with the User, by accepting its input and showing the contents of 
the Model, and operates on it in **read-only**. Being the face of the
application, it is also the one that is more likely to change and adapt, often
under pressure of non-programming factors such as visual design and usability
needs.

A View holds the following responsibilities:

- handle "purely GUI" intelligence, like behavior on
  resizing, repainting (e.g. on showing the window), data displaying and 
  visual formatting. 
- handle and dispatch primary events such as mouse clicks and keyboard key
  presses
- listens for Model notifications and responds by fetching and repainting
  the new state from the Model (reactivity). 

A View should not:

- perform directly any modifying action on the Model as a consequence to UI events. 
  Instead, they should delegate this task to Controllers. 
- perform any operation that is competence of the Model, nor store Model data, except 
  for caching to improve rendering performance. Cached data are never authoritative, 
  and should never be pushed back into the Model, or handed out to other objects. 

A View is generally composed out of reusable, generic visual building blocks called 
**Widgets**. Examples of widgets are buttons, checkboxes, and menus. 
Widgets, differently from Views, are not reactive: they have no concept of
Model nor of notification listening. Their visual content is modified by means of 
method calls. Complex UI interfaces are assembled from a collection of
Widgets, hierarchically contained in dialogs, windows and other visual
containers. The resulting UI becomes a View when Model observing capabilities
are added.

---
**Note**

MVC is not only limited to GUI representations, and Views are not necessarily
graphical objects. In fact, anything that can report information to the User in
some form can be classified as a View. For example, a musical notation Model
can be observed by two Views: one that shows the musical notation on screen and
another that plays it on the speakers. 
---


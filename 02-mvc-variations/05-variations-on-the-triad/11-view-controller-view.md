---
grand_parent: 2 MVC Variations
parent: 2.5 Variations on the triad
nav_order: 11
---
# 2.5.11 View-Controller-View

A View-Controller-View is basically a Model-Controller-View where one of the
Views is playing the part of the Model for a specific interaction. This occurs
when a View must interact with another View to orchestrate its behavior.  A
simple practical example is a Dialog for a Search functionality, and an Editor
providing methods for this functionality. The two Views must interact so that
when the user clicks on the “Search” button of the Dialog, the Editor is
directed to perform the search. 


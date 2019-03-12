---
title: MVC Variations 
nav_order: 3
has_children: true
permalink: /03-mvc-variations/
---
# MVC Variations

Traditional MVC is excellent as a starting point for discussion, but by no
means it must be considered the one and only proper way of doing MVC. In fact,
we saw how Traditional MVC is outdated within the context of modern UI
development. New patterns have emerged, built around fundamental MVC concepts 
and nomenclature, but with additional tricks, extensions and alternative design
choices to satisfy modern requirements, such as the following:

   - a modal dialog must allow changing values, but revert them when the Cancel
     button is pressed.
   - a modeless dialog allows changing values while the change is visible in
     another window, but must be reverted if “Restore” is pressed.
   - prevent typing of invalid values, for example a string in a line edit
     supposed to accept only digits will not accept any key presses from
     non-digits.
   - alternatively, allow invalid entries, but disable the Ok button and mark
     the incorrect value red.
   - and so on...

As you can see, the complexity of an application made of hundreds of menus,
text input areas and buttons, plus all the possible logical dependencies among
them can grow considerably. Unexpected interactions and strange communication
patterns emerge in the form of bugs or application freezes. Keeping this
communication network well organized and confined by enforcing a structure is
of paramount importance.

Additionally you might have to fight your toolkit because it prefers a specific
implementation of MVC.

Design aims at managing complexity. The MVC details given in this book are
guidelines, but need to consider the actual real problem at hand. Some
flexibility is needed. Strict compliance generally produces a benefit, and has
better communicative consistency within the development team, but may not scale
up to specific cases. In that case, reconsider the design, or relax some
constraints, but aim at keeping logic encapsulated and object interaction
simple and straightforward.

In this chapter we will examine alternative design in MVC able to deal with
more complex use-case scenarios, constrained by requirements, architectural
needs or self-documentation purposes.


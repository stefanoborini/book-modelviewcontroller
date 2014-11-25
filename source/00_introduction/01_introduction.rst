Introduction
============

Model-View-Controller (MVC) is probably the most used pattern for User
interface design and web programming; first defined at the end of the 70s, it
progressively adapted and morphed into a wide range of subtypes and variations,
so much that the term "MVC" is no longer specific enough to talk about the
pattern. In fact, the word "pattern" is probably not appropriate for MVC.
Instead, it can be seen as a rather loose guideline for organizing your code
when the data part and the visualization part of your application need to
interact while staying as loosely coupled as possible. MVC is implemented
through an aggregation of more fundamental design patterns such as Composite,
Mediator and Observer/Notifier. The complexity and variation in style of MVC
arises from all the possible uses and variations of these independent patterns
to satisfy the potentially elaborate requirements of a GUI. 

The objective of this book is to explore variations and nuances of MVC,
comparing and analyzing them. I will talk about "MVC" generically to refer to
all its different incarnations, and with a more specific name to refer to
specific ones. As you will observe in the upcoming sections, the common point
of all variations is to decide “who is responsible for what” and “who knows
about whom” in the interaction between User and Application data. Different MVC
variations assign responsibilities in a different way, connect or organize
protagonists in a different way, or add intermediate objects to gain more
flexibility and satisfy peculiar use cases.

This book is structured as follows:

    - The first chapter will start from the simplest form of GUI with state: the
      Smart-UI. We will then progressively refactor Smart-UI into a
      “Traditional MVC”, followed by a definition of its components, roles,
      and communication patterns.

    - Once equipped with nomenclature, the second chapter will introduce
      variations of Traditional MVC to address specific constraints and
      practical needs.

    - The third chapter will expand the concept of MVC to hierarchical MVC schemes.

    - In the fourth chapter we will focus on special collateral techniques that
      may emerge from a complex modern GUI.

    - In the fifth and final chapter, we will specifically focus on Web MVC and
      its implementations.


All the example code here presented will be Python, using the excellent Qt4
toolkit through PyQt4.  Qt provides pre-made mechanisms to address most of our
needs, but in the upcoming code these mechanisms will occasionally be skipped
on purpose to demonstrate a more general approach.

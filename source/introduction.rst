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
through an aggregation of design patterns such as Composite, Mediator and
Observer/Notifier. The complexity and variation in style of MVC arises from all
the possible uses and variations of these independent patterns to satisfy
potentially elaborate requirements of the GUI. 

The objective of this writing is to explore variations and nuances of MVC,
comparing and analyzing them. I will talk about "MVC" generically to refer to
all its different incarnations, and with a more specific name to refer to
specific ones. As you will observe in the upcoming sections, the common point
of all variations is to decide “who is responsible for what” and “who knows
about whom” in the interaction between User and Application data. Different MVC
variations assign responsibilities in a different way, connect or organize
protagonists in a different way, or add intermediate objects to gain more
flexibility and satisfy peculiar use cases.

This book is structured with the objective of justifying each new design
variation with a practical need. We will go from the most trivial to more
complex designs in a step-by-step fashion. The resulting organization will be
as follows:

    - The first chapter will start from the simplest form of GUI with state, a
      Smart-UI, and refactor it progressively into a so-called “Traditional MVC”. We
      will then provide a formal definition of Traditional MVC components, detailing
      their roles and communication patterns.

    - Once equipped with nomenclature and an array of cases, the second
      chapter will introduce variations of Traditional MVC to address specific
      constraints.

    - The third chapter will expand the concept of MVC to hierarchical MVC schemes.

    - In the fourth chapter we will focus on special collateral techniques that
      may emerge from a complex modern GUI

    - In the fifth and final chapter, we will specifically focus on Web MVC and its implementations.

All the example code here presented will be Python, using the excellent Qt4
toolkit though PyQt4.  Qt provides pre-made mechanisms to address most of our
needs, but in the upcoming code these mechanisms will occasionally be skipped
on purpose to present a more general approach.

The problem
-----------

The aim of GUI programming is to provide an interactive and updated visual
representation of the current state of the application. A typical set of
requirements is the need to simultaneously represent this state graphically in
various forms (i.e. a table of numbers and an XY plot), modify this state
through an unpredictable sequence of mouse/keyboard events, and keep the state
and its visual representation always synchronized and up-to-date. At the same
time, the application state must respect business logic constraints and be kept
within these constraints. At the code level, these requirements are generally
translated into objects interacting through a communication network of various
degrees of complexity. How can we satisfy these requirements, while at the same
time providing a flexible design that keeps the object communication simple,
understandable and organized as much as possible?

MVC addresses the above needs. It does so by clever subdivision of competences
and roles in the code, while introducing constraints that keep a potentially
chaotic communication well organized and streamlined. MVC is incredibly
flexible and adaptable, as we will see, and using one of the many styles will
be a matter of preference or constraints/best practices of the development
framework of choice. 

The guidelines given here are a collection of design solutions, best practices,
and experiments made available by countless blog posts and comments. This works
collects, organizes and enriches those contributes to provide a single source
of knowledge for those who want to understand MVC and its variations. 


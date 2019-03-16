---
title: 1.4 In depth analysis of MVC roles
parent: 1 Basics of MVC
nav_order: 4
has_children: true
permalink: /01-basics-of-mvc/04-in-depth-analysis-of-mvc-roles/
summary: Explaining Model, View, and Controller individual responsibilities
---
# 1.4 In depth analysis of MVC roles

In the previous sections we performed a progressive refactoring from Smart UI, 
to Document-View, and finally to Traditional MVC. This refactoring was driven
by the need for additional flexibility, separation of concerns and
clarification of the different roles. **MVC is, at its core, an exercise in data
synchronization between the Model and the View.** The MVC roles help us giving 
structure to the communication traffic needed by this synchronization ballet.

To summarize the scope of each role in Traditional MVC:

   - **Model**: holds the application's state and core functionality (Domain logic).
   - **View**: visually renders the Model to the User (Presentation logic).
   - **Controller**: mediates User actions on the GUI to drive modifications on the Model (Application logic).

Except for the most trivial applications, multiple classes can be active in the
same role and are said to belong to a specific **layer** (i.e. Model layer, View
layer and Controller layer). Objects from these layers are composed into **MVC
Triads** that give rise to the final application's behavior and aspect.  This
design is blessed with technical advantages: 

   - The clear separation of concerns between data storage, data handling, data
     visualization, and user interaction opens the possibility to be flexible
     in changing their implementation (for example, the layout of the graphical
     interface).

   - The communication among objects is restricted on purpose and characterized
     by its triad interaction pattern, reducing complexity and side effects.

   - Applications that need to visualize the same data in different ways, or
     modify them from different sources (for example, a data table and a plot)
     can do so while keeping the information centralized and synchronized.

   - Separation of concerns leads to easier testability and thus higher
     reliability: each component can be tested independently from the others,
     with their dependencies replaced by mock objects with predictable behavior.

   - Frameworks and GUI toolkits already provide MVC solutions as part of their
     design: you just have to “fill the blanks” to get a working application. 

Additionally, MVC accelerates development, improves readability and communication of intent: 

   - Different teams with different skills can work in parallel on separate
     parts of the application: frontend developers and GUI designers can work
     on the visual aspect, while backend developers and storage scaling specialists
     can work on low-level data representation. 

   - By defining clear interfaces on the protagonists' classes, the code
     documents itself both through the API and their role within the MVC design

   - MVC provides a common vocabulary to talk about roles and responsibilities
     in design.

A large application is composed of many different triads, each ideally
decoupled from the others, except at the Model level.


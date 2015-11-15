# Basics of MVC: From Smart-UI to Traditional MVC

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

GUI Programming is a complex task. Many different levels of understanding 
and handling are needed: UI design and usability consideration,
multithreading and multiprocessing for asynchronous evaluation, 
event notification coherence and balancing, adaptability of the GUI
to unexpected requests and changes of style. There are plenty of 
dialogs, buttons, lists, all with different performance, presentation and
visibility needs. In a sense, a GUI application develops emerging
properties characteristic of a complex system where multiple entities
interact. Keeping this system under strict control is the only
way to maintain chaos at bay. 

In this chapter, we will start from the most trivial implementation
of a GUI application with both visual and non-visual logic: a single class
responsible for everything. This approach, known as Smart UI, will be our 
foundation for a progressive refactoring into the three basic components 
of MVC: Model, View and Controller.

   * [Smart UI](01_smart_ui.md)
   * [Document View](02_document_view.md)
   * [Traditional MVC](03_traditional_mvc.md)
   * [In depth analysis of MVC roles](04_in_depth_analysis_roles.md)
       * [Model](05_model.md)
       * [View](06_view.md)
       * [Controller](07_controller.md)
   * [Forces outdating traditional MVC](08_outdating_forces.md)

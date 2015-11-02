# Introduction

Model-View-Controller (MVC) is probably the most used architectural solution
for User Interface design and web programming; First defined at the end of the
70s, MVC has been progressively adapted and morphed into a wide range of
subtypes and variations, so much that the plain term "MVC" without additional
qualifications has lost specificity. As a general interpretation, it is a
rather loose guideline for organizing your code when the data and visualization
parts of your application need to interact while staying as loosely coupled as
possible. How this is accomplished in practice depends on the particular MVC
incarnation.

MVC can be seen as an aggregation of more fundamental design patterns
such as Composite, Mediator and Observer/Notifier. The complexity and variation
in style of MVC arises from all the possible uses and variations of these
independent patterns to satisfy the potentially elaborate requirements of a
GUI. 

The objective of this book is to explore variations and nuances of MVC,
comparing and analyzing them. I will talk about "MVC" generically to refer to
all its different incarnations, and with a more specific name to refer to
specific ones. The common point of all variations is to decide “who is
responsible for what” and “who knows about whom” in the interaction between
User and Application data. Different MVC variations assign responsibilities in
a different way, connect or organize protagonists in a different way, or add
intermediate objects to gain more flexibility and satisfy peculiar use cases.

This book is structured as follows:

- The first chapter will be a gentle introduction to MVC through code examples, 
  with the objective of deploying a common vocabulary. It will start from the 
  simplest form of GUI with state, the Smart-UI, and progressively refactor it 
  into a “Traditional MVC”. The chapter will continue with a definition of 
  the MVC components, roles, and communication patterns, and close with a remark
  about the outdated nature of the "Traditional MVC" in modern software development.

- Once equipped with nomenclature, the second chapter will introduce
  variations of Traditional MVC to address specific constraints and
  practical needs. It will focus on variations of the three protagonists of MVC
  (Model, View, and Controller) and their interaction.

- The third chapter will expand the concept of MVC to hierarchical MVC schemes.

- The fourth chapter will focus on special techniques that emerge from a 
  complex modern GUI.

- In the fifth and final chapter, we will specifically focus on Web MVC and
  its implementations.

Throughout the book, some example code in Python will be used to clarify design
ideas. GUI rendering will make use of the excellent Qt toolkit, through PyQt4.
Qt provides pre-made mechanisms to address some MVC needs, but in the
upcoming code these mechanisms will be skipped on purpose to demonstrate the
presented concepts.

### Acknowledgements and motivations

I started writing this book as an accident. Initially, I wanted to write a
series of blog posts to describe Model View Controller and a few related
patterns.  As I gathered more and more information from the net and my personal
experience, I suddenly found out that the amount and structure of what I wrote
was beyond the scope of a blog, hence the decision to re-label it as a book. I
am happy with the decision, because it gave me freedom to add material I would
not have added otherwise.

This works presents and enriches design solutions, best practices, and
experiments made available by countless blog posts and comments. To these 
authors goes my acknowledgement and gratitude.  Being a work in progress,
there's still a lot to be done. Please be patient, but feel free to send me
feedback, pull requests, and take advantage of the material already present. 

This book is released under GFDL license, and free (gratis), mainly for three 
reasons

 - As stated, most of the material here presented was gathered from the net.
   It was my personal effort to organize this knowledge, but I had
   a lower startup barrier.

 - I already [published a book with a commercial publisher](http://www.amazon.com/Computing-Comparative-Microbial-Genomics-Microbiologists/dp/1849967636), 
   and from my experience and math, I think that if I put a book on the 
   web and accept donations I would probably get more money and feedback than
   going through a publisher.

 - This book is part of my portfolio as a professional in software development
   and design, and I am proud to focus on a personal project to increase my
   competences.

That said, I gladly accept donations:

 - on [GratiPay](https://gratipay.com/StefanoBorini/)
 - on [bitcoin](bitcoin:13RQmVjRKVbQnVmuVsFxHjycgo7cTaaZ3w)
 - on PayPal (using my email address stefano.borini at ferrara dot linux dot it)

The sources of this book are available as a github repository at the following
URL:

https://github.com/stefanoborini/modelviewcontroller-src

I also have a personal website at http://forthescience.org where you can find
more information about me, my curriculum and activities.

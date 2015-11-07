# Data/Metadata Model

### Motivation

A Data/Metadata Model separates its provided information in two parts:

    - *data*: slow, heavyweight information that represents the content
    - *metadata*: fast, lightweight information that describes the content

This distinction is often driven by the need for a Model object to represent
and provide access to large information for processing while also providing 
lean access to minimal information for browsing.

### Design

The Model class implement getters for both data and metadata. Clarity
in documentation is essential to guarantee that users of the class 
are aware of the associated cost of invoking the method.

Data methods retrieve the information lazily. Caching may not be possible,

Metadata methods may or may not be lazy, and may use caching, especially
when backed by network.

### Practical Example

An image processing program may have a `Picture` Model object
to represent an image file on the disk. `Picture` may provide methods 
such as `name()`, `size()`, `thumbnail()`, which represent lean 
information useful for a picture browser, and `data()` which retrieves
the bulk of the picture data from the disk and makes it available for
processing. When instantiated, `Picture` retrieves just the lightweight 
information from its backend.

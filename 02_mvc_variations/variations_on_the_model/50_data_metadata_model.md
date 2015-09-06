# Data/Metadata Model

A Data/Metadata Model separates its provided information in two parts:

- *data*: slow, heavyweight information that represents the content
- *metadata*: fast, lightweight information that describes the content

This distinction is often driven by the need for a Model object to represent
and provide access to large information for processing while also providing 
lean access to minimal information for browsing.

For example, an image processing program may have a `Picture` Model object
to represent a picture file on the disk. `Picture` may provide methods 
such as `name()`, `size()`, `thumbnail()`, which represent lean 
information useful for a picture browser, and `data()` which retrieves
the bulk of the picture data from the disk and makes it available for
processing. When instantiated, `Picture` retrieves just the lightweight 
information from its backend.

The same approach can be used to differentiate information
requiring reduced network access from information requiring large data transfers.


<!--- Done -->
# Data/Metadata Model

### Motivation

A Data/Metadata Model separates information in two categories:

- *data*: slow, heavyweight information that represents the content
- *metadata*: fast, lightweight information that describes the content

This distinction is often driven by the need for a Model object to 
present lean access to information needed for browsing, and resource consuming
access to information needed for processing.

### Design

The Model class implement getters for both data and metadata. 

- Data methods retrieve the information lazily, possibly in chunks. 
  Caching may not be possible if the size of the information is excessive.
- Metadata methods may or may not be lazily retrieved, and may use caching, 
  especially when backed by network.

Clarity in documentation is essential to communicate the associated cost 
of retrieval.

### Practical Example

An image processing program may have a ``Movie`` Model object
to represent an image file on disk

```python
class Movie(Model):
    def __init__(self, filename):
        self._filename = filename
        self._thumbnail = _extract_thumbnail(filename)
        self._length = _extract_length(filename)
        self._name = _extract_name(filename)

    # Metadata
    def thumbnail(self):
        return self._thumbnail

    # <similar getters for the remaining metadata>

    # Data
    def contents(self):
        # <...> 
```

Properties such as ``thumbnail``, ``length`` and ``name`` represent lean 
information useful for a movie browser. This information is extracted 
from the file at object instantiation and kept in memory.

The ``contents()`` method, on the other hand, retrieves the movie data 
directly from the disk and makes it available for additional processing 
(e.g. decoding and displaying).

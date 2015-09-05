# Caching model

Models may want to cache information when acting as a proxy for data sources
that are slow, unreliable, or have an access quota or cost. Typical examples are
network services, databases, disk access, or when long running computations are
needed to generate the information. 

A cache delivers an improvement in perceived performance and reliability, 
but comes with a set of liabilities.

- Increases memory footprint of the application.
- when reading from the Model, the View may retrieve outdated information. This is of particular importance


reduces network traffic
When 
- when accessing a remote resource, prevents repeated
  requests of the same resource. Failure to implement caching in this case may result
  in excessive network traffic.






Interested listeners of the Model may or may not need to be aware of the existence of
a cache. Using a cache generally gives a faster response after the first
access, improving the perceived performance.


When writing, the action can be funneled directly to the source, or performed on the cache.
The cache must prevent eviction of dirty information.

The implementing class simply retrieves the information from the data source,
stores it into an internal container, and returns it. A subsequent request for
the same data will return the cached information, instead of accessing the data
source again.

LRU cache


loading only information that is relevant, withholding bulkier
information, but providing a mechanism to access it once needed.
(FIXME maybe move to advanced techniques? where does it fit?)

How to outdate the cache?
timestamp retrieval

preemptive caching.

Store data instead of retrieving them again and again. Need a good index based on the
request parameters so that the proper entity is retrieved. Old entries may need to be discarded
usually in a least frequently used fashion. However, considerations about time to generate
may also be important. Better to throw away more disk retrieved data in favour of keeping
a network retrieved data.


Aim at a trade off between memory and processor usage, caching only the minimal information to save cache space, whenever possible, at the cost of some processor usage. 

Expiration of the cached information: by absolute timeout (e.g. 15 minutes), by sliding timeout (e.g. 5 minutes, but reset the timer if requested again. potentially never refreshed), or by external event (e.g. method call that forces cleanup).

Caches for information that needs to be written back to the database may offer
a challenge. When the data is retrieved, it's stored in the cache. When it's written,
the cache for that entry must be invalidated, otherwise we would retrieve the cached entry.

In multi-user applications or web applications, it's important that some type of cached
entries are not delivered to a user they were not intended for. Some critical
information may be into it.


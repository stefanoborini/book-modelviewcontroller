Caching model
-------------

Models that need to access slow or unreliable data sources such as disks,
databases, or web endpoints often use a caching strategy to improve performance
and reliability, trading memory occupation for computational time or network
access.

The implementing class simply retrieves the information from the data source, stores it into an
internal container, and returns it. A subsequent request for the same data will return the cached
information, instead of accessing the data source again.

LRU cache


loading only information that is relevant, withholding bulkier
information, but providing a mechanism to access it once needed.
(FIXME maybe move to advanced techniques? where does it fit?)

How to outdate the cache?

Store data instead of retrieving them again and again. Need a good index based on the
request parameters so that the proper entity is retrieved. Old entries may need to be discarded
usually in a least frequently used fashion. However, considerations about time to generate
may also be important. Better to throw away more disk retrieved data in favour of keeping
a network retrieved data.

Saves hammering to websites.

Aim at a trade off between memory and processor usage, caching only the minimal information to save cache space, whenever possible, at the cost of some processor usage. 

Expiration of the cached information: by absolute timeout (e.g. 15 minutes), by sliding timeout (e.g. 5 minutes, but reset the timer if requested again. potentially never refreshed), or by external event (e.g. method call that forces cleanup).

Caches for information that needs to be written back to the database may offer
a challenge. When the data is retrieved, it's stored in the cache. When it's written,
the cache for that entry must be invalidated, otherwise we would retrieve the cached entry.

In multi-user applications or web applications, it's important that some type of cached
entries are not delivered to a user they were not intended for. Some critical
information may be into it.


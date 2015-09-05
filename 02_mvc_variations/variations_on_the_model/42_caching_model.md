# Caching Model

Models may want to cache information when acting as a proxy for 
data sources that are slow, unreliable, or have an access quota 
or cost. Typical examples are network services, databases, disk
access, or when long-running computations are needed to generate
the information. 

Using a cache generally delivers the following advantages

- gives a faster response after the first access, improving 
  the perceived performance of the application.
- Neutralizes potential temporary failures of the data source,
  improving perceived reliability.
- when accessing a remote resource, prevents repeated requests 
  of the resource (known as "hammering"). Failure to 
  implement caching in this case generally leads to a security 
  response (throttling, or access ban) from the administrators 
  of the remote resource.

However, caching comes with a set of liabilities:

- Increases memory footprint of the application to store the cached data.
- the Model may return outdated information to its client. 


This is of particular importance

## Design


<p align="center">
    <img src="images/caching_model/caching_model.png">
</p>

The typical design of a Caching Model involves the following steps while getting data:

1. The View attempts to retrieve some information from the Model.
2. The Model first attempts to obtain this information from the Cache.
3. If the desired information is not found, the Model will perform
   a query to the slow data source, obtain the result, add it to
   the Cache, and return it to the View.
4. Additional attempts to retrieve the same information from the Model
   will extract data from the Cache.


When parameters are passed during the `get` request, the cache must 
have an index over these parameters to guarantee a retrieval of the
intended information. For example, if a Model class `UserRepository` 
has a method `get_user_data(user_id)`, this method must use the
parameter `user_id` to perform the intended retrieval from the cache.

When setting data on the Model, the possible strategies are 

1. always perform the changing action on the slow data source, 
   followed by either a similar update on the cached data, or an
   invalidation of the cached data.
2. just update the cached data, delaying the slow data source update
   until later.

Both strategies come with caveats. For the first one, 
if the `set` action is expected to change the data source in 
a non-trivial way, it may not be possible to perform a sensible 
change to the cached data with the same business logic supported 
by the remote source. Instead, one should remove the cached data 
to promote a fresh retrieval at the next `get` operation. 

Another caveat is that the operation always requires a round trip to 
the slow data source. This has consequences both at the UI level
(failures must be reported, in-progress operations need to present
a sensible progress bar, perceived performance may suffer) and also
at the application design level (if repeated `set` operations 
are needed, performing a round trip to the data source every time
is wasteful and impacts performance)

The second strategy may seem to solve some of the problems
given above: changes are kept local to the application when
actively changed, and the data source access cost is paid 
later, possibly as a bundled single change request.
The cache, however, must not evict the changed information 
until it has been committed to the data source. Further issues
may exist for resources that are shared among clients, or in case
of application crash or network failure where the changed content 
is only partially submitted or not at all.

Interested listeners of the Model may or may not need to be aware 
of the existence of a cache. 

## Caching strategies

Choosing an appropriate Caching strategy is a complex topic 
and outside the scope of this book. A trivial strategy
is to discard the Least Recently Used (LRU) data and replace it
with new data. This approach constraints the size of the cache 
to a given value and keeps the most recently used data in the cache, 
but does not provide a predictable expiration strategy.

Expiration of the cached information: by absolute timeout (e.g. 15 minutes), by sliding timeout (e.g. 5 minutes, but reset the timer if requested again. potentially never refreshed), or by external event (e.g. method call that forces cleanup).



Data/Metadata model
loading only information that is relevant, withholding bulkier
information, but providing a mechanism to access it once needed.
(FIXME maybe move to advanced techniques? where does it fit?)

How to outdate the cache?
timestamp retrieval

preemptive caching.


Aim at a trade off between memory and processor usage, caching only the minimal information to save cache space, whenever possible, at the cost of some processor usage. 


In multi-user applications or web applications, it's important that some type of cached
entries are not delivered to a user they were not intended for. Some critical
information may be into it.


Memoization is probably the most trivial form of Caching Model.

However, considerations about time to generate
may also be important. Better to throw away more disk retrieved data in favour of keeping
a network retrieved data.
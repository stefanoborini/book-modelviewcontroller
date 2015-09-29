# Caching Model

### Motivation

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
In multi-user applications or web applications, it's important that some type of cached entries are not delivered to a user they were not intended for. Some critical information may be into it.

## Design

The typical design of a Caching Model involves the following steps to
retrieve the data from a data source:

1. The View attempts to retrieve some information from the Model.
2. The Model first attempts to obtain this information from the Cache.
3. If the desired information is not found, the Model will perform
   a query to the data source, obtain the result, add it to
   the Cache, and return it to the View.
4. Additional attempts to retrieve the same information from the Model
   will extract data from the Cache.

<p align="center">
    <img src="images/caching_model/caching_model.png">
</p>

When parameters are passed during the `get` request, the cache must 
have an index over these parameters to guarantee a retrieval of the
intended information. For example, if a Model class `UserRepository` 
has a method `get_user_data(user_id)`, this method must use the
parameter `user_id` to perform the intended retrieval from the cache.

To set data on the Model, two strategies are possible:

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
of the existence of a cache. If the listener can behave appropriately 
by ignoring the existence of the cache Several strategies are possible to handle this 

## Caching strategies

Choosing an appropriate caching strategy is a complex topic 
well outside the scope of this book. Several factors may need to be kept into
account, such as data access patterns, specific requirements of the design 
and the application behavior, and data consistency.

To present a few among many possibilities, the most trivial strategy
is to simply perform memoization of the result. A Model using memoization
effectively uses a cache whose entries never expire. The cache size can be
kept under control by discarding the Least Recently Used (LRU) data.
This approach constraints the size of the cache and keeps the most recently 
used data in the cache, but does not provide a predictable expiration strategy.

Predictable expiration may be a requirement for some applications. For example,
a News Ticker application retrieving information from a website may want to
invalidate the cached data and perform a new retrieval, hopefully to obtain
updated information, after a fixed absolute timeout (e.g. 15 minutes).
Other applications may prefer cached data to expire only if not accessed 
within a given amount of time (e.g. 5 minutes, but the countdown resets 
to zero if requested again), or when an explicit method call is issued 
on the Model object. Smarter strategies may use a small payload request
to ask the remote service if new or changed data are available, and act
accordingly by either retrieving the new data or return the cached information.

Additional optimization may come from preemptive caching of model data
that is likely to be accessed soon. For example, while retrieving information about a given user from a social networking website, a smart caching engine 
may decide to retrieve its most recent pictures and populate the cache of the
picture Model objects.


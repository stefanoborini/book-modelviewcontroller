# Proxy Model

-----------
**Note**: In the context of Qt MVC, a Proxy Model is a Model Pipe design.

-----------

### Motivation

We want to access an external resource, such as one provided by an HTTP 
server or a database. Proxy Model encapsulate the logic needed to access 
the remote service, specifically:

- issue the request to the remote service
- handle error conditions
- convert received data into a representation useful for the client code.

Additionally, the Proxy Model can:

- Throttle an excessive number of requests in a short amount of time
- Cache obtained results and manage the cache expiration
- Observe the remote service for changes, for example through
  polling on a secondary thread.

### Design

The design of a Proxy Model is generally dependent on the service it 
represents. Interfaces are designed to comply with the abstraction of the
remote service. When the client code asks for data, the Model issues the 
appropriate request to the service provider.

### Practical example

Django Models are an example of a Proxy Model. Data is backed by a database,
generally SQL. Each Model class is represented as a database table, with columns 
being the Model instances. Model instances retrieve and store information to the 
SQL database through SQL statements created and issued by the Django backend code.
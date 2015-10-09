# Recording Model

### Motivation

Recording Model records every time there's a change in its state, and writes
down what has changed, for external consumption.

Simple implementation, a set that is zeroed on demand, and every time a set
command is called, that attribute name is added to the set.

alternative: add to the set at every invocation of a attribute setter (zeroing
every time). This will mean only one entry at a time, unless the Model implements 
a transactional change.

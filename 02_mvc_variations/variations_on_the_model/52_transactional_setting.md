# Transactional Setting

### Motivation

Your Model has multiple settable attributes, each one listened independently by Views. You want to change the Model state, and the logic needs to do so requires to set many of these attributes. Every set operation would trigger a notification. The behavior would be

 1. Set A attribute on the Model
 2. Views are notified of A change
 3. Set B attribute on the Model
 4. Views are notified of B change

During step 2, listeners will be notified of the change and sync against a Model where only one of the attributes has been changed. Depending on the specific details of your Model and Views, this state may be inconsistent or not representable by your Views. 

What is needed is to perform notification of the changes only when all set operations have been performed, 


    Set A
    Set B
    Notify A change
    Notify B change

instead of 




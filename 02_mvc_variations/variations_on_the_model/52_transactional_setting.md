# Transactional Setting

### Motivation

Having an object that requires change of multiple attributes with notification
done after both changes. 
E.g. 

    Set A
    Set B
    Notify A change
    Notify B change

instead of 

    Set A
    Notify A change
    Set B
    Notify B change



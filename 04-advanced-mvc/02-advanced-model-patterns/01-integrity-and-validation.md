---
grand_parent: 4 Advanced MVC
parent: 4.2 Advanced Model Patterns
nav_order: 1
---
# 4.2.1 Integrity and Validation

Model objects must often ensure three levels of conformity in their state:

- property integrity: the data must conform basic constraints for a specific property of the model.
- property validation: the overall model state must be appropriate.
- model validation: the overall model state must be appropriate.

Property integrity ensures that type and basic validity checking are respected. For example, a Model 
with the property ``customer_age`` will accept positive numbers, but refuse to accept strings or negative 
numbers, and typically raise an Exception when asked to do so. The View can provide support to enforce this 
integrity by restricting what the user can type (for example, only numbers), but the Model has ultimate 
responsibility to enforce this integrity. Appropriate mechanisms must ensure that, if the Model rejects
the change, the View restores the current value for that property.

Property validation is less strict, and focuses on the internal conformance of a given property
with a predefined schema. A typical example is an ``email`` property. While the valid content for this 
property must contain an @ symbol, the user must be able to potentially set the property to an intermediate
 string that does not contain that symbol, for example while the email is being typed. Typically, Property 
 validation is performed either "as the user types" or when the UI field loses focus. The UI can hint the user
 about the improper value, either with a popup, an icon or a red-colored field.

Finally, Model Validation performs cross validation between properties to ensure an overall consistency
of the content of the model for further use and processing, and is generally performed when the overall state is 
committed (e.g. by pressing OK). Typical example is to ensure that properties ``min`` and ``max`` are indeed
numerically consistent with ``min < max``. One should resist the temptation to enforce these checks as 
Property validation level, for two reasons: the logic may become complex, and the temptation to introduce smart 
behaviors such as trying to fix the values for the user is high. Unfortunately, this may result in UIs that 
deceive and annoy the user by changing values by themselves, possibly making a valid
state unreachable because the user is prevented from using invalid states as "stepping stones".

Validity might depend on the expected task. A Model for a text editor may contain an invalid 
python program, but that should not prevent the application from saving it as a file. It may however 
prevent the editor from executing it.

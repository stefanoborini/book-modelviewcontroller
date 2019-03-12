---
grand_parent: Advanced MVC
parent: Advanced Model Patterns
nav_order: 18
---
# Synchronous vs. Asynchronous Model

In general, it's better to have a synchronous model. Blocking allows you to decide the threading policy.
if you have an asynchronous model, you are stuck with the threading policy defined by the model,
which may not be optimal. Also, it makes testing harder.

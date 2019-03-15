---
grand_parent: 4 Advanced MVC
parent: 4.2 Advanced Model Patterns
nav_order: 18
---
# 4.2.4 Synchronous vs. Asynchronous Model

In general, it's better to have a synchronous model. Blocking allows you to decide the threading policy.
if you have an asynchronous model, you are stuck with the threading policy defined by the model,
which may not be optimal. Also, it makes testing harder.

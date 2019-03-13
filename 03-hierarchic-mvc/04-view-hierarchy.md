---
parent: 3 Hierarchic MVC
nav_order: 4
---

# 3.4 View Hierarchy

Views have a natural containment relationship. One View (the superview) may contain other "sub-Views". The hierarchy is,
first and foremost, visual. This hierarchy generally has consequences on how controllers are designed and structured,
and can also have consequences on how Models are designed, although in principle they should not depend on visual
concepts.

Example: simple weather forecast?

---
parent: MVC on the web
nav_order: 8
---
Models should:

- handle communication with the data source
- handle validation
- should be free of anything related to the web request (e.g. GET/POST variables) or response cycle (e.g. HTML rendering)

Views should:

- Handle end-user rendering (e.g. HTML/JS) and other presentation code (e.g. code to traverse data for rendering purposes).
- Should be free of anything related to the web request (e.g. GET/POST variables)
- should be free of any interaction with the data source

Controllers

- handle web request operations
- handles Model object creation 



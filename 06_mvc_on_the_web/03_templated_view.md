---
parent: MVC on the web
---
Templated View
--------------

To render the contents of the model, normally but not exclusively in HTML, a
template View is used. The template is a blueprint document, containing HTML
mixed with placeholder tags. These tags are replaced when the controller applies 
model's data to the template, producing the final HTML content.

This mechanism isolates the data from the production of HTML. It also allows
to select a different template if the same data must be delivered in a different
form (e.g. JSON, or XML) or for a different device (HTML for a computer vs. 
for a cellphone). Template authors don't need to know the framework, but they can focus
on the visual result, while controller authors don't need to worry about
visual issues, and focus instead on passing the needed data to the template.

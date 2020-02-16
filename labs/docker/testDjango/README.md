# Simple app using django
## Nick Kelly
### February 15, 2020

### Introduction
To gain a better understanding of Django - the server side framework we will be using - I followed a [tutorial](https://docs.djangoproject.com/en/3.0/intro/tutorial01/) on how to create a simple web application which used data from a database. I do have experience with web development but this is my first time using python/django in a project. 

### What I learned

##### Models
As I was working through the tutorial the first thing that surprised me was how easy it was to create tables in a database. Tables in django are described as a [model](./polls/models.py). Each field in a model corresponds to a field in a database. When a model is made a corresponding table will be created in the database that is being used. A database abstraction API is used to make queries on the records in the table. To create a record in the table all the programmer has to do is make an object of the model.

##### Templates
Templates are the way in which django dynamically creates webpages. The process is similar to PHP where the code is embedded in the HTML code. Variables are surrounded by two curly braces on either side. The variables are passed to the template through a 'context' which is included when the creation of the template is initialized. Tags allow for the programmer to control the logic that is displayed through the template. Tags include this like for loops, if statements and many more. Django templates have the ability to inherit from other templates so if the website has a similar layout across multiple pages a base template can be made and each page can extend upon the base template. 

##### Views
Views deteremine what the default action will be once a web page is accessed. It most cases all the view will do is setup a context and initialize a template but the functionality can be extended. The view can be used to access information from a database or handle form data.
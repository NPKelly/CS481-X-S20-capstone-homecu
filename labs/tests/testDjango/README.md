# Testing within Django
## Nick Kelly
### February 16, 2020

### Introduction
As the size of an application grows, the need of a automated test suite also grows. Typically when I am testing an application I run it several times with expected and unexpected inputs and see what the results are. This is not an effective or efficient way of testing and it doesn't guarantee that the defects are found. Using practices such as Test Driven Development and Unit Testing will ensure that the defects that are introduced through coding will be minimal and the overall quality of the application will be better. To learn more about making and running tests in Django I followed a [guide](https://docs.djangoproject.com/en/3.0/intro/tutorial05/) which discussed the ways to test models, views, and the philosophy behind writing tests.

### Running the tests
Required:
* Python 3.X.X
* Django 3.0.3

In the [testApp](./testApp/) directory run the following command:
```
$ python manage.py test polls
```

When this command is run, the Django framework will look for subclasses of the Django.test.TestCase class and then run any methods with a name beginning with 'test'. A special database is created so the tests do not interfere with any established data.

The results of the tests will appear after all of completed.

### What I learned

##### Testing Models
Models are Django's method for creating and interacting with the data in a table. The small application that I made to learn about Django has two models, one of which has a function that returns whether or not a question was created in the past 24 hours. In order to test this function a subclass of the Django.test.TestCase class had to be made. This subclass will hold all the test cases that relate to the Question model. Three test functions were written (each beginning with 'test') to ensure that only questions with publication dates within the past 24 hours will be marked as 'recent'. 

##### Testing Views
Testing views is a little more tricky because to effectively test a view a user has to be simulated. Django handles this by providing a Client which simulates a user interacting with the code. When testing a view it is important to check the response of the webpage to know if the correct things are being displayed when the user connects. 

##### Future Testing
It is very important to create tests for any potential weaknesses that your program may have. With all of these tests it is easy for them to get messy and jumbled. To organize tests within the [tests.py file](./testapp/polls/tests.py) each view or model should have its own subclass of TestClass, each test condition should have its own test method, and the test methods should have clear names which describe there function.
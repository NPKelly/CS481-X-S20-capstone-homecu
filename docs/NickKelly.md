# Nick Kelly Weekly progress report

## Week 1

## Week 2

Created teams and met with teammates.

## Week 3

### January 28, 2020

Wrote questions to ask during the sponsor meet up that is taking place on 1/30. Had a short meetup with Shane to discuss documenting individual contribution throughout the project.

### January 30, 2020

Sat in on a meeting with the sponsor of the project to discuss an overview of the features that are to be implemented. Future meetings will take place on Thursdays at 1:30 PM. Notes that I took on the meeting will be uploaded.

### February 1, 2020

Wrote short descriptions on the features that are to be implemented throughout the course of the project. 

## Week 4

### February 4, 2020

Met with the team to get a better understanding schedule for the rest of the semester. Wrote an outline for the team-created schedule for the semester. Will need to meet with the team/instructor/sponsor to make sure the schedule is not missing anything.

### February 6, 2020

Met with the sponsor to discuss the docker environment and the schedule going forward.

### February 7, 2020

Applied the github patch that the sponsor provided to the repository.

## Week 5

### February 10, 2020

I spent time installing docker and understanding the environment. I ran into a lot of issue when installing docker but was able to overcome most of them. The main issue that I faced was that my computer does not support Hyper-V. This feature is only in Windows 10 Pro and Enterprise editions. I had to use Docker Toolbox instead of the main docker program. From what I can see Docker Toolbox works fine with the provide docker container. I will discuss with the other team members about how their docker setup went tomorrow.

### February 11, 2020

Turns out the previous attempts at getting docker to work on my machine were not successful, but I was able to get it working. Instead of using Docker Toolbox on my Windows 10 environment I used a VM running Ubuntu. This worked flawlessly. I used a guide by Nick Janetakis to [set up the VM](https://nickjanetakis.com/blog/create-an-awesome-linux-development-environment-in-windows-with-vmware) and to [get docker setup](https://nickjanetakis.com/blog/docker-tip-73-connecting-to-a-remote-docker-daemon).

### February 12, 2020

Updated the main README.md of the repository to match our schedule and added directories to /labs to match the updated schedule.

### February 15, 2020

I worked through a tutorial to get a better understanding of the django framework. The code for the app can be found [here](../labs/docker/testDjango/) and a write up of what I learned can be found [here](../labs/docker/testDjango/README.md).

### February 16, 2020

I worked through a guide on testing django applications. I learned that all testing of the django side of our application will take place in a file called tests.py. This file will contains subclasses of the django.test.TestCase for each of the models/views/etc. that we will test. This file may get crowded with classes and function so it will be important to keep a consistent naming scheme and documentation.

## Week 6

### February 18, 2020

This week I am going to create flow diagrams that show the general user interaction with the web site. These will include basic information about the features the user will interact with and the purpose that the features have. There will be small descriptions about the required inputs the user needs to make and the functions that the server side application will need to implement to handle the requests. Today I completed the flow diagram for the login feature.

### February 23, 2020

I worked more on the flow diagrams completing the flow diagrams for the list of credit union feature and the manage users feature. I also updated the login feature flow diagram with the mockups made by Nealon Hager.


## Week 7

### February 25, 2020

This week we begin development on the various features that we have been planning on making. Today I create tasks for the user stories defined for these features.

### February 26, 2020

I created some more tasks based on the user stories that we have selected for the first "Sprint". I also worked on one of the tasks which required me to generate Model representations of each table in our database. 

### February 27, 2020

The first task that I assigned myself to is to authenticate users when they attempt to log in. I researched how django handles things like retrieving information from the database and how passwords are hashed. It turns out django has a functionality called a User model which handles simple user creation and user authentication. To incorporate this model into our project I will have to extend this model so it fits with the user table that the sponsor provided us. 


## Week 8

### March 2, 2020

Today I began implementing the User Verification feature for our login. Extending the AbstractBaseUser model was not difficult. Slight modifications had to be made to the database schema such as renaming 'username' to 'user_name', these probably could have been avoided but I could not find a solution. After the AbstractBaseUser model was extended a UserManager had to be created to handle actions that affect the users in the table such as queries on the DB. As development progressed I got to the point of taking input from the user. This is where I am currently blocked and I am researching the ways to handle input and authenticate it against the User models. 


### March 3, 2020

Today I researched ways to avoid changing the schema of the database. I contacted our sponsor to ask if it was okay to change the schema of the database. They said that it was fine but handing off the project after it is completed would be easier if the schema didn't change. If we are going to use the AbstractBase User as we planned there is no way to avoid changing the schema. Through my research the only way to avoid it is to use authentication on the database. The database provided by the sponsor does not offer this so I am forced to change the schema of the database.

### March 8, 2020

Finally finished the user authentication system for the login page. The problem that I was having was caused by the database appending whitespace to the end of the password field. When the password checking function would pull the user's password from the database the extra whitespace would invalidate the password match. I fixed this by altering the schema of the 'bsu_officeusers' table of the database. I changed the data type of the password and user_name fields from 'character(X)' to 'character varying(X)'.


## Week 9

### March 10, 2020

Met with the team and the instructor to review our progress throughout the semester. Overall our group is doing fantastic with only minor deficiencies. After the meeting I created a small prompt that informs the users that the supplied username and password are invalid. I also made a small python script to insert users into the db.

## Week 10

### March 16, 2020

One of the features that the sponsor wanted was a secure login. I had already implemented the authentication of the users but one more step to make the login secure was to implement a block for brute force attacks. If a user fails to enter the correct password for the specified username five times in a row, that username will be blocked from logging in for 5 minutes. After the five minute wait time, if the user enters an incorrect password the five minutes will start over. With these precautionary steps the login system is more secure.



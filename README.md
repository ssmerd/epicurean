# Epicure Junction

![am I responsive screenshot](readme/amiresponsive.png)

## A restaurant website.
> A themed restaurant website showcasing the venue and menu. The site allows to book one or more guests for a meal in a restaurant and a particular time and date. The site should alo avoid double bookings and allows multiple table occupancies. In order to book a table or tables, a user needs to sign up and/or login. 




### - By Sebastian Smerd

## **[Live site](https://restaurant-epicurean-a32b57262b21.herokuapp.com/)**

Note: 

The website has performance issues dut to the database used in the project. Elephant SQL Postgress is very slow.

## **[Repository](https://github.com/ssmerd/epicurean)**


  
## Table of contents

 1. [Database](#database)
 2. [UX](#ux)
 3. [Agile Development](#agile)
 4. [Features](#features)   
 5. [Technology used](#technology) 
 6. [Testing](#testing)  
 7. [Deployment](#deployment)
 8. [Credits](#credits) 
 9. [Acknowledgements](#acknowledgements)  
 



## Database

> Database Structure

![ERD Diagram](readme/erd.png)

The ERD diagram shows the logical structure of the database used in the project. I converted it to the ORM model used in Django. This, next, was converted by Django to physical structure in the Postgress database. It is important that the restaurant table must be configured before the application is used. It has to contain a row for every individual table, with its number and number of seats.


### Database Schema

#### Booking

| id | Field |
|--|--|
| name | Charfield |
| email | Charfield |
| phone| CharField|
| no_of_people | IntegerField |
| message | CharField | 

---

#### Table

| id | Field |
|--|--|
| number | IntegerField |
| no_of_seats | IntegerField|


---

#### BookingTable


| id | Field |
|--|--|
| booking_date | DateField|
| booking_time | TimeField|



# UX

## Overview

Epicure Junction is a fictional restaurant. The main goal of the website is to allow users to view some photos of the venue, see what they have to offer, view the menu and if it is to their liking then the user can create an account and use it to make reservation requests.

### Design

I decided that I wanted this website to be modern, minimalistic in it's appearance. 

### Site User

 - Someone within the same city as the restaurant looking for new places to visit
 - Someone who would prefer to make bookings digitally rather than speaking with others

###  Goals for the website

 - To allow customers to see their menus ahead of time
 - To allow customers to make bookings through the website 
 

## Wireframes

###  Wireframes

> Main page


![Index page](readme/wireframe.png)

My goal for this project was to create a simple sleek website that allowed the restaurant to showcase it's venue and menu. I intentionally ensure the number of pages was at a minimum to ensure the core functionality was the focus.


# Agile 

### Agile Overview

This project was started alongside a GitHub Projects Page to track and manage the expected workload ahead.
The aim was to set out my expected workload, list the epics and then break them down into user stories or bite sized tasks to work towards and ultimately finish the site in good time.

To see Kanban please click [here](https://github.com/users/ssmerd/projects/2).


#### User stories

#####  Completed User Stories

To view any of the expanded details of the user stories please click on a user story below to be taken to the Kanban project.


 1. [USER STORY: Create a restaurant website](https://github.com/ssmerd/epicurean/issues/1)
 2. [USER STORY: A customer signs up and/or logs in to the website](https://github.com/ssmerd/epicurean/issues/2)
 3. [USER STORY: Book a table](https://github.com/ssmerd/epicurean/issues/3)

The following User stories were not completed as they were deemed to be not necessary for this project at this time but are indications of possible future features:

 ##### Extra User stories
 
 1. [USER STORY: View my reservations]
 2. [USER STORY: Cancel my reservations]
 3. [USER STORY: Owner can view current reservations]
 4. [USER STORY: Owner can cancel current reservations]

---

# Features


#### User based Features Implemented:

 - **Users can** navigate the restaurant website
 - **Users can** create an account
 - **Users can** sign up and/or log into their account
 - **Users can** log out of their account
 - **Users can** make a booking through the reservation form 

#### Account restrictions:

 - **Users cannot** access the reservation form until they sign up or login
 

#### Website features:



### Main website

#### Desktop

> Desktop Navigation

![Main page](readme/hero.png)

 - The desktop navigation consists of a Home, About, Menu and Contact. 
 - A user can sign up, log in or book a table from this website.
 - If a user isn't logged in, and presses book a table, the login page will pop up

---

> About page

![About page](readme/about.png)


---

> Menu page

![Menu page](readme/menu.png)


---

> Book a table page

![Book a table](readme/form.png)

- The form can be used to book a table or tables by a user
- A user can book multiple tables if the number of user don't fit in one table
- A user can only book a table from 11am till 11pm
- One booking is for one hour
- A user can send an optional message

---

> Contact

![Contact](readme/contact.png)

  

---

## Features left to Implement 


 - Add ability for customers to view and cancel their bookings
 - Add ability for a restaurant owner to see all the bookings
 - Add ability for a restaurant owner to cancel bookings
 - Send an email to a customer with their reservations


---


# Technology

- Html

- CSS

- JavaScript

- Python

- Django

- Font Awesome

- Bootstrap 5

- Jinja 

- GitHub

- Heroku

- Elephant PostgreSQL

- Cloudinary

- Git

- JQuery Timepicker

- Google Fonts

- Isotope JS library



---


## Testing


### Testing Phase


#### Account Registration Tests
| Test |Result  |
|--|--|
| User can sign up | Pass |
| User can log into account| Pass|
|User can log out of account|Pass|

---

#### User Navigation Tests

| Test |Result  |
|--|--|
|User can navigate to Reservations | Pass |
|User can access menu items| Pass|


---

#### Account Security Tests

| Test |Result  |
|--|--|
|Non logged in user cannot make reservation | Pass |


---

#### Booking Tests

| Test |Result  |
|--|--|
|User can make a booking when all fields complete | Pass |
|User tries to submit booking with empty fields |Fail|
|User tries to submit over book |Fail|


---

## Google Lighthouse Testing

### Desktop


![Google Lighthouse](readme/lighthouse.png)

- When the database is deployed on Elephant SQL performance is poor
- When the database is local the performance is very good.

## HTML W3 Validation

### Main page

[W3 Validation checker](https://validator.w3.org/nu/?doc=https%3A%2F%2Frestaurant-epicurean-a32b57262b21.herokuapp.com)

#### Result: No Errors

### CSS Validatio

[w3 Jigsaw CSS checker](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Frestaurant-epicurean-a32b57262b21.herokuapp.com)

#### Result: Pass - No Errors


---


---


# Deployment

To deploy the project through Heroku I followed these steps:

- Sign up / Log in to  [Heroku](https://www.heroku.com/)
- From the main Heroku Dashboard page select 'New' and then 'Create New App'
- Give the project a name 
- After this you select select create app. 
- The name for the app must be unique or you will not be able to continue.
- Heroku will create the app and bring you to the deploy tab. 
- From the submenu at the top, navigate to the resources tab.
- Click on the setting tab
- Open the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
- Inside the Django app repository create a new file called env.py
- within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Elephant SQL. 
- The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
-   Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
-   Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
-   In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
-   insert the line if os.path.isfile("env.py"): import env
-   remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
-   replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
-   In the terminal migrate the models over to the new database connection

-   Navigate in a browser to cloudinary, log in, or create an account and log in.
-   From the dashboard - copy the CLOUDINARY_URL to the clipboard
-   In the env.py file - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"
-   In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars
-   Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
-   this key value pair must be removed prior to final deployment
-   Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staitcfiles' and 'cloudinary' goes below it.
-   in the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
-   Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
-   Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
-   Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
-   In your code editor, create three new top level folders, media, static, templates
-   Create a new file on the top level directory - Procfile
-   Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi
-   In the terminal, add the changed files, commit and push to GitHub
-   In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
-   Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

#### Forking the repository

By forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository.
You can do this by: 
-  Logging into GitHub or create an account. 
- Locate the repository at  [here](https://github.com/ssmerd/epicurean)  . 
-  At the top of the repository, on the right side of the page, select "Fork" from the buttons available. 
-  A copy of the repository should now be created in your own repository.


---

# Credits 
  
##### https://bootstrapmade.com/delicious-free-restaurant-bootstrap-theme/

  - I used some ideas from the template. But I changed a lot to fit my purpose.
  - I used JS library from the template. I added my own Js too.
  
##### Unsplash

  - The images used in this project come from unsplash website.

##### Code Institute

##### Django Documentation

# Acknowledgements

* Cohort Facilitator - Special credit to Alan Bushell who gave great support and tips when testing the website.
* The tutors at Code institute


<a href="#top">BACK TO TOP 🔼</a>

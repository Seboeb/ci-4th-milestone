[![Build Status](https://travis-ci.org/Seboeb/ci_4th_milestone.svg?branch=develop)](https://travis-ci.org/Seboeb/ci_4th_milestone)
# Tasting Experience - Development
This project is build for users of the [The Tasting Experience Finder](https://github.com/Seboeb/ci-2nd-milestone) app and [The Tasting Experience Recipes](https://github.com/Seboeb/ci-3rd-milestone) community website. Since these projects are new and still under development, there is a high probability that some bugs are present. This project provides a platform where users can submit bugs that they have found and keep track of reported issues (also from other users). The cool thing is, that not only bugs can be reported but new feature requests as well!

At [this](https://the-tasting-experience-dev.herokuapp.com/) website you can see all reported bugs and feature requests and start adding new ones of yourself.

## UX
This project has a mobile first approach. The website must provide a clear landing page where the users get a first impression of the goal of this website. Users must be able to subscribe and, subsequently, create an account. Bug reports and feature requests can be found via the navigation bar. After logging in users are able to create bug reports and feature request. User must be able to see a clear overview of all the issues and, where possible, see graphs of the development progress.

![design mockup](https://github.com/Seboeb/ci_4th_milestone/blob/develop/media/mockup.jpg)

A mockup is made with the use of Figma. [Here](https://www.figma.com/file/Eftlt380cS1zJEdY9fVJEISq/The-tasting-experience?node-id=0%3A1) you can find the full design.

### User Stories
- As a user I want to be able to subscribe and, subsequently, login to the website.
- As a user I want to be able to create a new bug report.
- As a user I want to be able to edit my bug report.
- As a user I want to create new feature request and select my prefered amount for donation.
- As a user I want to upvote existing bug reports of other users.
- As a user I want to upvote/donate a feature request that I want to request myself.
- As a user I want to be able to create comments on bug reports or feature request.
- As a user I want to see an overview of all the reported bugs and see the severity of that bug.
- As a user I want to see an overview of the requested features and the current state of the donation.
- As a user I want to see a list of features that are in active development.
- As a user I want to be able to navigate to the tasting experience finder app and the online recipe community website.

## Features
Here you can see the features that are already implemented and which are left to implement in this project.

### Existing Features
The user can: 
- Create an account for the Tasting Experience Development website
- Login as a registered user
- Change his password when he forgets
- Select a profile avatar and edit personal details
- Subscribe to a newsletter
- See a list of tickets for the finder app and recipe community of the tasting experience
- Search for specific tickets, name, id's, status, ...
- Create a new bug report and can edit it
- Create a new feature request and can edit it
- Add a ticket to his watchlist
- Upvote a ticket
- Comment on a ticket
- Make a donation for a feature request
- See reporting statistics

### Features Left to Implement
There are some usefull features that could be implemented, but aren't implemented at this moment.  
- Edit a comment of your own.
- Upload images with your bug report or feature request
- Color indication for the status of the tickets in the global ticket list.
- Share tickets on social media.

## Technologies Used
This project uses several existing third party technologies to improve code quality and to speed up the development time. The following tools are used:
- **[Python](https://www.python.org/)**
    - Python is a programming language that lets you work quickly and integrate systems more effectively
- **[Django](https://www.djangoproject.com/)**
    - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Note, this project uses Django version 1.11.
- **[JQuery](https://jquery.com/)**
    - JQuery makes things like HTML document traversal and manipulation, event handling, animation, and Ajax much simpler with an easy-to-use API that works across a multitude of browsers.
- **[NodeJs](https://nodejs.org/en/)**
    - Node is designed to build scalable network applications. It will be used to run the webpack builder for client JavaScript.
- **[npm](https://www.npmjs.com/)**
    - npm is the package manager for JavaScript and the world’s largest software registry. It will be used to manage all the javaScript dependencies used in this project.
- **[webpack](https://webpack.js.org/)**
    - Webpack is a build tool that puts all of your assets, including JavaScript, images, fonts, and CSS, in a dependency graph.
- **[Handlebars](https://handlebarsjs.com/)**
    - Handlebars provides the power necessary to let you build semantic templates effectively. It is used to improve UX experience during AJAX calls.
- **[Heroku](https://www.heroku.com/)**
    - Heroku is a cloud platform as a service (PaaS) that lets companies build, deliver, monitor, and scale apps.
- **[Travis CI](https://travis-ci.org/)**
    - Travis CI is a hosted continuous integration service used to build and test software projects hosted at GitHub.
- **[Cypress](https://www.cypress.io/)**
    - Cypress is a Javascript End to End testing framework. In contrast to Puppeteer, which is a library, Cypress gives you a solid platform for writing and automating UI tests.
- **[Stripe](https://www.stripe.com/)**
    - Stripe is an American technology company based in San Francisco, California. Its software allows individuals and businesses to make and receive payments over the Internet.

Additionally, the following webpack modules are used:
- **babel-loader, babel/core, babel/preset-env**
    - These modules are used to convert modern ES6 JavaScript files into robust ES5 JavaScript files which is supported on any browser.
- **handlebars-loader**


## Database Model
This project uses a SQL type database and PostgreSQL to be specific. [Here](https://www.postgresql.org/) you can find more about MySQL. This project uses the following database tables:
- **User**
    - In this table the information about the user is stored, e.g. name, email, password.
- **UserRole**
    - In this table user roles are defined, such as developer, end user or admin.
- **Donation**
    - In this table payments/donations for feature requests are stored.
- **Comment**
    - This table holds all the comments of users.
- **Ticket**
    - Each feature request or bug report is stored in a ticket table.
- **TicketProgressLabel**
    - The status of the tickets are stored in a ticket progress label table.
- **TicketPriorityLabel**
    - Each tickets has a specific priority which is stored in this table.
- **TicketType**
    - There are two ticket types so far, feature requests and bug reports.

A detailed overview of the table structure and data types can be seen in the [database_schema](https://github.com/Seboeb/ci_4th_milestone/tree/develop/database_schema) folder.

## Installing Guide
This project uses NodeJs for managing the Javascript libraries, webpack and a testing application. Visite their [website](https://nodejs.org/en/) to install NodeJs for your operation system. NodeJs ships with npm, which will be automatically installed.

In order to install the JavaScript dependecies in this project, please clone the repository to a folder on your computer. Open a terminal (or command prompt) and cd into your cloned folder. Type in the following command:
```
npm install
```
This command will install all the module dependencies that are listed in the package.json file. 

Since the webserver runs on Django, which is a web framework for Python, it is necessary to install Python from their [website](https://www.python.org/). When installing Python, pip is automatically installed as well. The latter is a package manager for Python. Open a terminal (or command prompt) and cd into your cloned folder. Type in the following command:
```
pip install -r requirements.txt
```
This command will install all the module dependencies that are listed in the requirements.txt. Please note that the actual install command for pip may vary based on your OS and Python version. 

Django uses the SQLite database technology as a standard. You can deside to use the standard provided SQLite or a different SQL database technology as you wish. When using a different database, please make sure that you update your Django settings accordingly. You can read the official documents [here](https://docs.djangoproject.com/en/1.11/ref/settings/#databases). *Note, when using a cloud database solution such as Heroku Postgres, make sure that you have ```dj-database-url``` installed via pip.

Okay so far great, you are almost done and the last thing you must do is to create the database structure and populate it with some initial data. Type the following command in your terminal in order to make migrations:
```
python manage.py makemigrations
```
There is a good chance that no changes are detected so far. Next, type the following command in order to migrate the database model tables to your database:
```
python manage.py migrate
```
The database is created with all its model tables. You have to load some inital data into the database using the folowing:
```
python manage.py loaddata initial_data_fixture.json
```
When the data is loaded you can make a superuser. This superuser is required for you to access the admin panel of this webapplication.
```
python manage.py createsuperuser
```
Fill in an email and password.

Make sure that you create your own ennvironment python file, you can find an example file in this repository. You are done and can run the project!
```
python manage.py runserver localhost:8080
```

## Testing
### Django tests
This project uses the build-in assertion testing from Django in order to test the models, forms, urls and its functions. The tests are written in the ```tests.py``` Python scripts in each application and to run the test, simply run the following command:
```
python manage.py test <application_name>
```
if you want to run specific application tests. When you want to run all tests use the following command:
```
python manage.py test
```
When the tests are successful, you should receive the an OK message in your terminal. If a test fails you can will see the details why it failed (see images below).

![Django tests](https://github.com/Seboeb/ci_4th_milestone/blob/develop/media/django_test.jpg)

![Django test failed](https://github.com/Seboeb/ci_4th_milestone/blob/develop/media/django_test_error.jpg)

### End to End tests
The Cypress Javascript tool is used in order to test the website in an end to end testing method. This testing method includes testing the client javascripts, but also the user interface. These tests are written in javascript in so called spec files. You can find these files over [here](https://github.com/Seboeb/ci_4th_milestone/tree/develop/cypress/integration). If you are interesed in writing your own test files or how it work, you can find more information at their [website](https://www.cypress.io/how-it-works/).

In order to run the Cypress test, you must install Cypress first. When you have followed the installation guide it is already installed during the npm install command. Otherwise you can install it via the command:
```
npm install cypress --save-dev
```
In order to start the test environment, execute the following command in your terminal:
```
cypress open
``` 
Cypress should open and by clicking on the "Run all specs" button, you testing begins :) Cypress provides good feedback whenever a test fails and includes the current state of the website per testing step. See the GIF image below for an impression.

![Cypress](https://github.com/Seboeb/ci_4th_milestone/blob/develop/media/cypress_test.gif)

All tests are green, which implies that the testing has been successful!

## Deployment
In order to make a production version of this project, you must edit some settings. Make sure that the **DEVELOPMENT** environment variable is removed. The next step is to setup the static file serving. You could use an external service that serves your static files, which is recommended. More information about this topic over [here](https://docs.djangoproject.com/en/1.11/howto/static-files/). 

This project has been deployed with Django it self as the static file server. If you want to do this by yourself, make sure that you run the following command in order to copy your assets in the static files folder:
```
python manage.py collectstatic
``` 
Do not forget to commit your changes before proceding. 

This project is deployed using Heroku and can be seen over [here](https://the-tasting-experience-dev.herokuapp.com/). Heroku is a cloud platform as a service supporting several programming languages. 

Follow the following steps to deploy this project to Heroku by yourself:

1. Create a Heroku account over [here](https://signup.heroku.com).
2. Create a new app and give it a name.
3. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
4. Open a terminal and login to heroku by using the ```heroku login``` command.
5. When successfully logged in, we have to add the remote heroku git repository. In the terminal, navigate to the root folder of your project. When git is not initialize, initialize it with ```git init```. In order to add the remote heroku repository you first have to navigate to the settings of your Heroku application. Under 'Info' you will find your Heroku Git URL (see image below). Copy this git url and execute the following command to add this remote repository to your local git.
```
git remote add heroku https://git.heroku.com/the-tasting-experience-dev.git
```
6. Make sure that you have included a ```requirements.txt``` and a ```Procfile``` in your projects root folder. An example ```Procfile``` can be found in the source files of this project. 
7. If you do not have an up-to-date ```requirements.txt``` file, create it using the following command:
```
pip freeze > requirements.txt
```
8. Now it is time to push your local git repository to your remote Heroku git repository by using the command below. Please note that ```master``` represents the git branche you want to push.
```
git push -u heroku master
```
9. The application is almost ready to be used on Heroku. Go to the settings tab and make sure you set the Config Vars. These variables are the environment parameters required for the application in order to run. Restart of the dyno may be necessary. See the image below which variables are required.

![heroku settings](https://github.com/Seboeb/ci_4th_milestone/blob/develop/media/heroku-settings.jpg)

## Develop on your own!
If you want to continue developing this project, you can do so by cloning this git repository. Make sure you install the project (see Installing) with the help of npm and pip. Make sure you configure the ```env.py``` file. The webpack config file is already good to go and does not need additional tweaks (but you can if you want). 

The main application ```ci_4th_milestone```. The JavaScript, scss and images are located in the ```static``` folder, as this folder is statically served by Django in debug mode. The html files have their own ```templates``` folder per application.

In order to build the JavaScript files using webpack, run the following command:
```
npm run build:webpack
```
and if you want to start the project run the command:
``` 
npm start
```
or
```
npm run start:win
```
when you are working on a Windows machine.

If you want to write your own testing cases, please add them to the ```tests.py``` file located in each of the applications folder. If you want additional End to End testing, you can do so by making new spec files located in ```cypress/integration``` folder.

## Credits
This project uses media and information from different sources. 

### Media
Images used in this project are grabbed from [pixabay](https://pixabay.com).

### Acknowledgements
This project uses a custom Django authentication User model. [This](https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username) article gives great information for you to follow.

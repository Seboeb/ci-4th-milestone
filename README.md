[![Build Status](https://travis-ci.org/Seboeb/ci_4th_milestone.svg?branch=develop)](https://travis-ci.org/Seboeb/ci_4th_milestone)
# Tasting Experience - Development
This project is build for users of the [The Tasting Experience Finder](https://github.com/Seboeb/ci-2nd-milestone) app and [The Tasting Experience Recipes](https://github.com/Seboeb/ci-3rd-milestone) community website. Since these projects are new and still under development, there is a high probability that some bugs are present. This project provides a platform where users can submit bugs that they have found and keep track of reported issues (also from other users). The cool thing is, that not only bugs can be reported but new feature requests as well!

At [this](https://the-tasting-experience-dev.herokuapp.com/) website you can see all reported bugs and feature requests and start adding new ones of yourself.

## UX
This project has a mobile first approach. The website must provide a clear landing page where the users get a first impression of the goal of this website. Users must be able to subscribe and, subsequently, create an account. Bug reports and feature requests can be found via the navigation bar. After logging in users are able to create bug reports and feature request. User must be able to see a clear overview of all the issues and, where possible, see graphs of the development progress.

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

A detailed overview of the table structure and data types can be seen in the [database_schema](https://github.com/Seboeb/ci-4th-milestone/tree/develop/database_schema) folder.

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

## Deployment
python manage.py collectstatic

## Develop on your own!

## Credits

  ### Media

  ### Acknowledgements
  https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username
  
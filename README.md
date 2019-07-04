[![Build Status](https://travis-ci.org/player64/Django-Issue-Tracker.svg?branch=master)](https://travis-ci.org/player64/Django-Issue-Tracker)

# Django - Issue Tracker
The app allows users to post report bugs and suggests new features. The users can create an account to enable posting  comments under bugs or features. There is a functionality to vote for the bugs, users can vote for the bug only once. Voting for functionalities require a fee of €50, which enables unlimited votes. Features with the highest number of votes will be developed and released in the next update. To inform users about the highest votes statistics there is a page displaying charts. The administrator of the website can mark bugs/features as following statuses: to do, doing, done.

## UX
The user needs to create an account to view/post features or bugs. After login to the app, the user is directed to  a profile page where users’ bugs & features are displayed.

### Statistic page
This page shows the statistics of features/bugs by status and most voted presented in chart format.

### Bugs / Features pages
This page displays reported bugs with brief information about the user, date posted and number of votes.

### Profile page
This page displays users’ added bugs and features.

### Blog page
This page shows the latest news

## Features
* Registered users can create the account and view/post about features & bugs.
* Users can't delete another user’s bug/feature or edit.
* Prevention of voting on a user’s own posted bug.
* Views are counted only once when users enter the recipe view - - if the page is refreshed it isn't counted.  This is done by session to prevent the collection of fake data.
* Users can vote for the feature by paying €50 for a vote; there is no limit to add multiple times.
* The profile page displays the user's posted bugs & features.
* Content on the website has been added by Python Faker.
* The project is using webpack for compiling scss files to css and ES6 scripts to ES5

## Features to implement
* Add pagination for bugs/feature
* Search bug / feature



## Technologies used
* HTML5
* [Django](https://www.djangoproject.com/)
    * for building app backend and render the frontend
* ES6 Support via [babel (v7)](https://babeljs.io/)
    * The project uses babel for compiling ES7 to ES5
* [Bootstrap 4](https://getbootstrap.com/)
    * Framework used for frontend development
* [JQuery](https://jquery.com/)
    * The project uses jquery for DOM manipulation and AJAX calls
* [SCSS](https://sass-lang.com/)
    * The project uses SCSS Preprocessors for compiling to CSS
* [Webpack](https://webpack.js.org/)
    * The project uses webpack for bundling the assets
* [Stripe](https://stripe.com/)
    * Used stripe gateway to proceed payments
* [Python faker](https://faker.readthedocs.io/en/latest/index.html)
    * It used to populate the fake content users/bugs/features/comments to run go to project folder python populator.py
* [Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    * Applying to Django forms bootstrap inputs textareas buttons classes
* Webpack loader
 
 ## Testing
* The app was developed by using Test Driven Development paradigm
* The website has been tested on various screen sizes

## Deployment
The application is deployed to [Heroku](https://django--issue-tracker.herokuapp.com/)

### Assets source files
Assets files are in assets folder

### Compiled files
Compiled files are in the compiled-static/webpack-bundle folder

### Installation
`npm install`

### Start Dev Server
`npm start`

### Build production version
When you run npm run build we use the mini-css-extract-plugin to move the css to a separate file. The CSS file gets included in the head of the index.html.

`npm run build`

## Credits
* Webpack [boilerplate](https://github.com/wbkd/webpack-starter)
* Images used from [Unsplash](https://unsplash.com/)
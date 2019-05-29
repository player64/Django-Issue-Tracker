[![Build Status](https://travis-ci.org/player64/Django-Issue-Tracker.svg?branch=master)](https://travis-ci.org/player64/Django-Issue-Tracker)

# Django - Issue Tracker
The app allows users to post report bugs and suggests new features. The users can create accounts posting the comments under bugs or features. There is a functionality to vote for the bugs, user can give only one vote for the bug only once. Voting for functionalities require a fee &euro;50 and is unlimited. The highest voted features will be developed and released in the next update. To inform users about the highest votes statistics page displaying charts in a common way. The administrator of the website could mark bugs/features as following statuses: to do, doing, done 

## UX
The user needs to create an account to view/post feature or bug. After login, it redirects to profile page where user's bug & features are displayed. 

### Statistic page
Showing the statistics about features/bugs by status and most voted presented in charts

### Bugs / Features pages
It's displaying the recent bugs with brief information about the user, posted date, number of votes, number of votes. 

### Profile page
It's displaying user's added bugs & features

## Features
* Registration user can create the account and view/post features & bugs
* Users can't delete someone bug/feature or edit
* Prevention of voting on own posted bug
* Views are counted only once when user enter the recipe view is incremented if refresh the page it isn't counted this is done by session to prevent the collection of fake data 
* User can vote for the feature by paying &euro;50 for a vote  there is no limit to add multiple times
* Profile page is displaying the user's posted bugs & features
* Content on the website has been added by python Faker
* Project is using webpack for compiling scss files to css ES6 scripts to ES5 it got implemented reloading when files changed.

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
* [Python faker](https://faker.readthedocs.io/en/latest/index.html)
    * It used to populate the fake content users/bugs/features/comments to run go to project folder python populator.py
* [Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    * Applying to Django forms bootstrap inputs textareas buttons classes
* Webpack loader
 
 ## Testing
* All the methods are covered at least in 70% by written unit tests
* Form unit test is written to check forms validation
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
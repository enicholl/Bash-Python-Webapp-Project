// required modules for the application to run
var express = require('express');
var path = require('path');
var routes = require('./routes/index');
var bodyParser = require('body-parser');
var helpers = require('./modules/helpers.js');

// saves express module as variable 'app'
var app = express();


app.locals.range = helpers.range;


// tells app to use pug as layout engine
app.engine('pug', require('pug').__express)

// tell the app to look for the pug files in the views folder
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

// required to collect data from html page using req.body
app.use(bodyParser.urlencoded({ extended: true }));
app.use('/', routes);

// exports all variables in this file to be used elsewhere
module.exports = app;


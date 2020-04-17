// requires the app file to start the application
var app = require('./app');

// starts the application on port 5000 and logs this in the console
var server = app.listen(5000, () => {
	console.log('Express is running on port 5000');
});

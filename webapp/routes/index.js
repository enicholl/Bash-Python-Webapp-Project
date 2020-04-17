// required modules saved as variables to be used in this file
var express = require('express');
var router = express.Router();
var {spawn} = require('child_process')


// defines the route to form and renders the response to the client
router.get('/', (req,res) => {
  res.render('form', { title: 'Game Page!' });
});

// post the results
router.post('/results', (req, res) => {
	// creates variable num from the input number from the user in form.pug
	var num = req.body.number;
	// creates function runScript() which returns output of catmice.py
	function runScript(){
		return spawn('python3', ['./python_scripts/catmice.py', num]);
	}
	// creates function dogScript() which returns the output of dog.py
	function dogScript(){
		return spawn('python3', ['./python_scripts/dog.py', num]);
	}
	// creates the function catScript() which returns the output of cat.py
	function catScript(){
		return spawn('python3', ['./python_scripts/cat.py', num]);
	}
	// creates the function mouseScript() which returns the output of mouse.py
	function mouseScript(){
		return spawn('python3', ['./python_scripts/mouse.py', num]);
	}
	// creates function camoScript() which returns the output of camo.py
	function camoScript(){
		return spawn('python3', ['./python_scripts/camo.py', num]);
	}
	// variables created to store the above function outputs
	var subcamo = camoScript()
	var submouse = mouseScript()
	var subcat = catScript()
	var subdog = dogScript()
	var subprocess = runScript()
	// variables of the output data ready to be sent to index.pug
	var dataToSend;
	var dogData;
	var catData;
	var mouseData;
	var camoData;
	// the below comments are the same for each 3 sections, 3 for each variable output
	// takes output of camo.py as variable 'data', inform the console, save output data to var camoData
	subcamo.stdout.on('data', (data) => {
		console.log("Doing the Cat & Mouse");
		camoData = data;
	});
	// if any errors occur reports them to the console
	subcamo.stderr.on('data', (data) => {
                console.log(`error:${data}`);
        });
	// closes the function output and logs into console
        subcamo.stderr.on('close', () => {
                console.log("Close Cat & Mouse");
        });
        submouse.stdout.on('data', (data) => {
                console.log("Doing the Mouse");
                mouseData = data;
        });
        submouse.stderr.on('data', (data) => {
                console.log(`error:${data}`);
        });
        submouse.stderr.on('close', () => {
                console.log("Close Mouse");
        });
	subcat.stdout.on('data', (data) => {
		console.log("Doing the cat");
		catData = data;
	});
	subcat.stderr.on('data', (data) => {
                console.log(`error:${data}`);
        });
        subcat.stderr.on('close', () => {
                console.log("Close cat");
        });
	subdog.stdout.on('data', (data) => {
		console.log("Doing the dog");
		dogData = data;
	});
	subdog.stderr.on('data', (data) => {
		console.log(`error:${data}`);
	});
	subdog.stderr.on('close', () => {
		console.log("Close dog");
	});
	subprocess.stdout.on('data', (data) => {
		console.log("Creating Python String");
		console.log(num);
		dataToSend = data.toString();
	});
	subprocess.stderr.on('data', (data) => {
		console.log(`error:${data}`);
	});
	subprocess.stderr.on('close', () => {
		console.log("Closed");
		// once all python processes completed and data stores, renders index.pug with the output vars included
		res.render('index', { results: dataToSend, dogs: dogData, cats: catData, mouse: mouseData, camo: camoData })
	});

});

// exports the router to be used in other files of the application
module.exports = router;

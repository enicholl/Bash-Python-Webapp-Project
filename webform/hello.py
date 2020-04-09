import flask
app = flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

if __name == "__main__":
	app.run()

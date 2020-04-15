from flask import Flask, render_template, request  # imports in necessary python modules and my other python files
from dog import dog
from catmo import camo
from mouse import mouse
from cat import cat
from catmice import cat_mouse
app = Flask(__name__)  # sets flask app to value app


@app.route("/")
def index():
    return render_template("Index.html")  # renders my index html page as the home page on localhost:5000


@app.route('/results', methods=['POST'])  # uses POST method to display outcome to /results page
def results_array():
    if request.method == 'POST':
        number = int(request.form['number'])  # saves value of number chosen by user as variable 'number'
        output = cat_mouse(number)  # saves results list to variable 'output'
        dogs = dog(number)  # saves number of dogs to variable 'dog'
        cats = cat(number)  # saves number of cats to variable 'cats'
        catm = camo(number)  # saves number of cat and mice to variable 'catm'
        mice = mouse(number)  # saves number of mice to variable 'mice'
        return render_template("Result.html", text=output, dog=dogs, cats=cats, mice=mice, catm=catm)
        # returns Result.html on /results page, uses variables within the brackets to transfer into the html code


if __name__ == "__main__":  # runs application
    app.run(debug=True)


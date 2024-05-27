from flask import Flask, render_template

# instantiate class "Flask":
# create program object "app"
app = Flask(__name__)

# 3
# simple data model
all_todos = [
    {
        "id": "5b4a3a09-33f7-4724-b7da-63478652a38c",
        "title": "Destroy the Death Start",
        "description": "Identify and hit with a  perfect shot the only one weak spot on a space ship as big as whole planet while avoiding bad guys. NOTE TO SELF: The targeting system sucks. Use the force.",
        "done": None,
    },
    {
        "id": "d3b4ace0-bcf0-4d45-a7dc-84199f667a26",
        "title": "Train with Yoda",
        "description": "There is no try; only do.",
        "done": None,
    },
]




# create a function for processing request
# officially called "view function"
# @app.route() is used as a decorator
# binding the relative URL to the function

# URL rule string
# "/" represents the root address
# we only needs the relative address, no port number and ip address needed
# e.g. if @app.route("/hello"), complete URL = localhost:5000/hello
# @app.route("/"), complete URL = localhost:5000
@app.route("/")
# 1
# When users visit this URL
# this function gets triggered
# fetches return value
# and displays the return value to the browser window
# 2
# flask will by default look for template files in `templates` folder
def index():
    return render_template("index.html")


@app.route("/todos", methods=["GET", "POST"])
def todos():
    return render_template("todos.html", todos=all_todos)





if __name__ == '__main__':
    app.debug = True
    app.run()

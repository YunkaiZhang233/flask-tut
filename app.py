from flask import Flask

# instantiate class "Flask":
# create program object "app"
app = Flask(__name__)


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
# When users visit this URL
# this function gets triggered
# fetches return value
# and displays the return value to the browser window
def index():
    return "<h1>TOTALLY USELESS APP<h1>"


if __name__ == '__main__':
    app.debug = True
    app.run()

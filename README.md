# Flask Tutorial, but Newest

This is an attempt trying to follow along the tutorial for Flask for DRP, but using the newer version of flask.

I will try to follow along Ivan's structure.

## Pre
Make sure you have Python3 on your machine.


## Running the app
To run the app:

```bash
# pre-process
python3.8 -m venv venv
source venv/bin/activate
pip install --upgrade pip && pip install -r requirements.txt
pip install python-dotenv

```

```bash

# configure environment variables to determine which program to run
export FLASK_APP=flask-tut/app.py 
# export FLASK_DEBUG=1 could be called here
# specify that we want to run in development mode
export FLASK_DEBUG=1
flask run
```
You can now browse to <http://localhost:5000> and see the app live.

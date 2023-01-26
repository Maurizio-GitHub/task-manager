# From our main taskmanager package, we import both 'app' and 'db':
from flask import render_template
from taskmanager import app, db


# To create a basic app route, we use the root-level directory of slash.
# This is used to target a function called 'home', which returns the
# rendered_template of 'base.html', our html template:
@app.route("/")
def home():
    return render_template("base.html")

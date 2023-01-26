"""
Whenever we modify our class-based models within 'models.py', we need to
migrate these changes as well, so the database knows about them:

We come here and navigate to the Terminal, log to the Postgres CLI by entering
'set_pg' first and 'psql' afterwards. Then, we enter the command
'CREATE DATABASE taskmanager;' and finally quit, as we need to use Python
to generate and migrate our class-based models into this new database - by
taking the models created for 'Category' and 'Task', and building the database
schema using the details therein provided. Therefore:

We enter the command 'python3', then the command 'from taskmanager import db'
and finally the command 'db.create_all()'. To exit the Python interpreter, we
simply enter 'exit()'.
"""

# From our main 'taskmanager' package, we import both 'app' and 'db'.
# To generate our database, we also need to import the classes that
# we defined as 'Category' and 'Task':
from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task


# To create a basic app route, we use the root-level directory of slash.
# This is used to target a function called 'home', which returns the
# rendered_template of 'base.html', our html template:
@app.route("/")
def home():
    return render_template("base.html")

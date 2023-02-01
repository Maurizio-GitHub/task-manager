"""
This is to initialize our taskmanager application as a package,
allowing us to use our own imports, as well as any standard imports.
"""
# After running 'pip3 install Flask-SQLAlchemy psycopg2' into Terminal:
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# To use any of our hidden environment variables, we need the 'env' package:
if os.path.exists("env.py"):
    import env

# We can now create an instance of the imported Flask() class, stored in a
# variable called 'app', which takes the default Flask __name__ module.
app = Flask(__name__)

# Then, we need to specify two app configuration variables.
# They both come from our environment variables:
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    # To ensure that SQLAlchemy can also read our external database,
    # its URL needs to start with "postgresql://":
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
        app.config["SQLALCHEMY_DATABASE_URI"] = uri

# We also need to create an instance of the imported SQLAlchemy() class,
# assigned to a variable of 'db' and set to the instance of our Flask 'app':
db = SQLAlchemy(app)

# Finally, from our 'taskmanager' package, we import the file called 'routes':
from taskmanager import routes

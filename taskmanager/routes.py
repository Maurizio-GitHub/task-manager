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
from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


# To create a basic app route, we use the root-level directory of slash.
# This is used to target a function called 'home', which returns the
# rendered_template of 'base.html', our html template:
@app.route("/")
def home():
    return render_template("tasks.html")


# In addition to returning the 'categories.html' template itself, this
# function queries our database. A new variable, 'categories' is defined.
# To query the imported 'Category' model ('models.py'), we opt for
# 'Category.query.all()' by adding the '.order_by()' method in between.
# Ordering by 'Category.category_name' avoids the default sorting (by ID).

# .all() method always goes to the end. It represents a Cursor Object, quite
# similar to an array or list of records. Sometimes, Cursor Objects can be
# confusing when used on front-end templates. Thankfully, there is a simple
# Python method to convert them into standard Python lists: 'lists()'.

# The 'categories=categories' represents a match between the variable name
# that can be used within the HTML template ('categories.html') and variable
# defined within our function (always keep naming convention consistent).

# Whenever we call this function by clicking on the link for 'Categories',
# it queries the database and retrieves all records from that table, sorted
# by category name. Finally, we need to pass this variable into our rendered
# template, so that this data can be used to display everything to our users:
@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


# When a user clicks to add a new category, this function renders the template
# that contains the form ('add_category.html'). By displaying the form this
# function leverages the "GET" method to get the page.
# However, when a user eventually submits the form to add a new category to
# our database, the function attempts to "POST" the data into the database
# by using the imported 'request', 'redirect' and 'url_for' methods:
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        # If the requested method is equal to POST, a new variable called
        # 'category' is created. It is set to a new instance of the Category()
        # model imported at the top of the file. By using the 'request'
        # method, we need to make sure that this Category() model uses the same
        # exact keys that it is expecting. For 'category_name', we can use the
        # requested form being posted to retrieve the name-attribute.
        # This is why it is important to keep the naming convention consistent,
        # meaning that our name-attribute matches that of our database model.
        # Once grabbed the form data, we can 'add' & 'commit' the information
        # to the SQLAlchemy database variable of 'db', imported at the top.
        # This uses the database sessionmaker instance. After the form gets
        # submitted, and we are adding & committing its data to our database,
        # we redirect the user back to the 'categories' page:
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")

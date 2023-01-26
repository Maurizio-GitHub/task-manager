"""
Normally, we have to import each table column type at the top of the file.
However, with Flask-SQLAlchemy, the 'db' variable contains each of those
already and we can use dot-notation to specify the data-type for our columns.

For each model, we also need to create a function called __repr__, which takes
itself as the argument (similarly to the 'this' keyword in JavaScript) and
representing itself in the form of a string.
"""

# We are defining our database, hence, we need to import
# 'db' from the main 'taskmanager' package:
from taskmanager import db


# Category table schema, via class-based model using SQLAlchemy's ORM:
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)

    # Not a column, not visible. It sets the referential integrity constraint
    # for this one-to-many relationship defined via a Foreign Key (see 'Task'):
    tasks = db.relationship(
        "Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.category_name


# Task table schema, via class-based model using SQLAlchemy's ORM:
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(
        "category.id", ondelete="CASCADE"), nullable=False)

    # In this case, we want to return multiple columns:
    def __repr__(self):
        return f"#{self.id} - Task:{self.task_name} | Urgent:{self.is_urgent}"

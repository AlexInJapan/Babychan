from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('todo.config')

db = SQLAlchemy(app)

from todo.views import views
from todo.views.todo_backend import confirm, input, list, result
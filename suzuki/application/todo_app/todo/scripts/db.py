from flask_script import Command
from todo import db
from todo.models.todo_list import Todo

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()
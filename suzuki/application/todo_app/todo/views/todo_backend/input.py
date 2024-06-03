from flask import request, redirect, url_for, render_template, flash, session
from todo import app
from todo import db
from todo.models.todo_list import Todo
from todo.views.views import login_required

@app.route('/')
@login_required
def input():
    return render_template('todo_frontend/input.html')
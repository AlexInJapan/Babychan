from flask import render_template, url_for, session
from todo import app
from todo.models.todo_list import Todo
from todo.views.views import login_required
from datetime import datetime, timedelta

@app.route('/list', methods=['POST', 'GET'])
@login_required
def show_todo():
    todo_list = Todo.query.order_by(Todo.todo_date.asc()).all()
    return render_template('todo_frontend/list.html', todo_list=todo_list)

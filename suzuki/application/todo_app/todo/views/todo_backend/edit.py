from flask import request, redirect, url_for, render_template, flash, session
from todo import app, db
from todo.models.todo_list import Todo
from todo.views.views import login_required

@app.route('/edit', methods=['POST', 'GET'])
@login_required
def edit_todo():
    edit_type = ""
    if request.form["button"] == "update_todo":
        edit_type = "update"
        edit_todo_list = request.args.getlist("edit_todo")
        session["update_todo_list"] = edit_todo_list
        return render_template(
            "todo_frontend/edit.html", 
            edit_type = edit_type,
            edit_todo_list=edit_todo_list)
    elif request.form["button"] == "delete_todo":
        edit_type = "delete"
        edit_todo_list = request.args.getlist("edit_todo")
        session["delete_todo_list"] = edit_todo_list
        return render_template(
            "todo_frontend/edit.html", 
            edit_type = edit_type,
            edit_todo_list=edit_todo_list)
    else:
        flash("エラー")
        return redirect('/')

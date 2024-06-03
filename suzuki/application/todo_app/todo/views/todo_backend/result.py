from flask import request, redirect, url_for, render_template, flash, session
from todo import app, db
from todo.models.todo_list import Todo
from todo.views.views import login_required
import random, string
from datetime import datetime


# ランダムな文字列を生成する関数を作成
def generate_id(n):
    return ''.join(random.choices(string.ascii_letters+string.digits, k=n))


@app.route('/result', methods=['POST', 'GET'])
@login_required
def update_todo():
    if request.form['button'] == 'add':
        todo = Todo(
            id=generate_id(8),
            todo_name=request.form['todo_name'],
            todo_date = datetime.strptime(
                request.form['todo_date'], "%Y-%m-%d").date(),
            todo_text=request.form['todo_text']  
        )
        db.session.add(todo)
        db.session.commit()
        flash('新しくToDoが追加されました')
        return redirect(url_for('input'))
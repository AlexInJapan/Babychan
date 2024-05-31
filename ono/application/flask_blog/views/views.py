from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from functools import wraps

def login_required(view):   #特定のビューにログイン認証を必要とするデコレーターを追加します。
                            #具体的には、ログインしていないユーザーがアクセスした場合にログインページへリダイレクトされます
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner


@app.route('/login',methods=['GET','POST'])
#/login という URL パスに対するビューを定義しています。
#HTTP メソッドが GET または POST の場合に処理が実行されます。
def login():
    if request.method == 'POST':    
    #POST メソッドでユーザーがフォームを送信した場合、ユーザー名とパスワードをチェックしてログイン状態を管理します
        if request.form['username'] != app.config['USERNAME']:
            flash("ユーザ名が異なります")
        elif request.form['password'] != app.config['PASSWORD']:
            flash("パスワードが異なります")
        else:
            session['logged_in'] = True
            flash('ログインしました')
            return redirect(url_for('show_entries'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('show_entries'))
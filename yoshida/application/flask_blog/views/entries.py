# ボタンを押した際の動作
from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_blog import db
from flask_blog.models.entries import Entry 
from flask_blog.views.views import login_required

@app.route("/")
@login_required
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template("entries/index.html",entries=entries)   


#ナビゲーションバーの給与計算を押すとcalc.htmlに遷移
@app.route("/entries/input",methods=["GET"])
@login_required
def input_entry():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("entries/input.html")

#ブログ新規投稿へ遷移
@app.route("/entries/new",methods=["GET"])
def new_entry():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("entries/new.html")


#計算するボタンを押した際、salaryのデータを送る
@app.route("/entries/input",methods=["POST","GET"])
def output_entry():
    salary = request.form["salary"]
    salary=int(salary)
    result = 0
    if salary > 1000000:
        result += (salary-1000000)*0.2 + 1000000*0.1
    else:
        result += salary*0.1
    return render_template('entries/output.html', 
                           salary = "{:,}".format(round(salary)), 
                           paid = "{:,}".format(round(salary-result)),
                           tax = "{:,}".format(round(result)))


#新しいブログ投稿ボタンを押した際の挙動
@app.route("/entries",methods=["POST"]) 
def add_entry():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    entry = Entry(
        title=request.form["title"],
        text=request.form["text"]
        )
    db.session.add(entry)
    db.session.commit()
    flash("新しく記事が作成されました")
    return redirect(url_for("show_entries"))

@app.route('/entries/<int:id>',methods=['GET'])
@login_required
def show_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    return render_template('entries/show.html',entry=entry)

@app.route('/entries/<int:id>/edit',methods=['GET'])
@login_required
def edit_entry(id):
    if  not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    return render_template('entries/edit.html',entry=entry)

@app.route('/entries/<int:id>/update',methods=['POST'])
@login_required
def update_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    entry.title = request.form['title']
    entry.text = request.form['text']
    db.session.merge(entry)
    db.session.commit()
    flash('記事が作成されました')
    return redirect(url_for('show_entries'))

@app.route('/entries/<int:id>/delete',methods=['POST'])
@login_required
def delete_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    flash('投稿が削除されました')
    return redirect(url_for('show_entries'))






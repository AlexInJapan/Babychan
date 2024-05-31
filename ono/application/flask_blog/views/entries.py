#ログイン関連のviewはこっち。記事に関連するviewはviews/views.py
from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_blog import db
from flask_blog.models.entries import Entry
from flask_blog.views.views import login_required

@app.route('/') #ユーザーがWebブラウザで /（ルートパス） にアクセスしたときに、show_entries()関数が呼び出される。
@login_required #ログインが必要なページであることを示す @login_required デコレーターで修飾されている
                #ユーザーがログインしていない場合、login ページにリダイレクトされる
def show_entries(): #データベースからエントリーを取得し、それを降順で並べ替えてテンプレートに渡しています。
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entries = Entry.query.order_by(Entry.id.desc()).all() #DBからすべての記事を取得し、新しく記事が作られた順にソート
    return render_template('entries/index.html', entries=entries)
    #entries/index.htmlで、DBから取得したすべての記事がentriesという名前で参照できる

@app.route('/entries', methods=['POST'])
#/entriesに POST リクエストが送信された場合に add_entry()関数が実行されます
@login_required
#ログインしていないユーザーがアクセスした場合にログインページへリダイレクトされるようにする
def add_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    #ログインしていないユーザーがアクセスした場合、ログインページへリダイレクトします。
    entry = Entry(
        title = request.form['title'],
        text = request.form['text']
    ) #フォームから送信された記事のタイトルとテキストを取得し、
      #models/entry.pyで作成したEntryモデル（クラス）を使ってEntry オブジェクト（インスタンス）を作成します
    db.session.add(entry)
    db.session.commit()
    #データベースに新しい記事を追加し、変更をコミットします。
    flash('新しく記事が作成されました')
    return redirect(url_for('show_entries')) #show_entries ビューへリダイレクトします

@app.route('/entries/new', methods=['GET'])
#entries/new.htmlにアクセスした場合に new_entry 関数が実行される
@login_required
def new_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/new.html')
    #ログインしているユーザーには、entries/new.html というテンプレートを表示

@app.route('/entries/<int:id>',methods=['GET']) #index.htmlのurl_forで渡された変数id
#この URL にアクセスされた場合、show_entry 関数が実行され、id という整数パラメーターを受け取る。
def show_entry(id):
    if not session.get('logged_in'): #Entry モデルから指定された id のエントリーを取得
        return redirect(url_for('login'))
    entry = Entry.query.get(id) #渡されたidの記事を（クエリで）DBから取得
    return render_template('entries/show.html',entry=entry) #entries/show.html テンプレートを表示

#以下、28章（Update）の内容
@app.route('/entries/<int:id>/edit',methods=['GET']) 
def edit_entry(id):
    if not session.get('logged_in'): 
        return redirect(url_for('login'))
    entry = Entry.query.get(id) 
    return render_template('entries/edit.html',entry=entry) 

@app.route('/entries/<int:id>/update',methods=['POST']) 
def update_entry(id):
    if not session.get('logged_in'): 
        return redirect(url_for('login'))
    entry = Entry.query.get(id) 
    entry.title = request.form['title']
    entry.text = request.form['text']
    db.session.merge(entry)
    db.session.commit()
    flash('記事が更新されました')
    return redirect(url_for('show_entries')) 

#以下、29章（Delete）の内容
@app.route('/entries/<int:id>/delete',methods=['POST']) 
def delete_entry(id):
    if not session.get('logged_in'): 
        return redirect(url_for('login'))
    entry = Entry.query.get(id) 
    db.session.delete(entry)
    db.session.commit()
    flash('投稿が削除されました')
    return redirect(url_for('show_entries')) 
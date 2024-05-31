from flask_blog import db
from datetime import datetime

class Entry(db.Model): #モデルはclassとして定義する。モデルにEntryという名前をつけている
    __tablename__ = 'entries' #実際のDBに格納されるテーブルの名前。ここではentriesというテーブル名
    id = db.Column(db.Integer,primary_key=True) #数字からなるidという属性名を主キーとして定義
    title = db.Column(db.String(50),unique=True) #titleは重複せず一意
    text = db.Column(db.Text) #大量のテキストを保持するときに使う
    created_at = db.Column(db.DateTime) #日付を保存するときに使う

    def __init__(self, title=None, text=None): #モデルが作成されたときの標準の動作
        self.title = title
        self.text = text
        self.created_at = datetime.utcnow()

    def __repr__(self): #参照されたときの表示フォーマットを定義
        return '<Entry id:{} title:{} text:{}>'.format(self.id,self.title,self.text)
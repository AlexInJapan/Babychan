from flask_script import Command
from flask_blog import db
from flask_blog.models.entries import Entry

class InitDB(Command): #script実行のためのクラス
    "create database" #クラスの説明のためのコメント

    def run(self): 
        db.create_all() #実際にスクリプトで実行される内容
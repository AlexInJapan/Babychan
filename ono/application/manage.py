from flask_script import Manager
from flask_blog import app
from flask_blog.scripts.db import InitDB #scripts/dbで定義したモジュール（クラス）をインポート

if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command('init_db', InitDB()) #initDBモジュールをinit_dbという名前で実行できる
    manager.run()  #ターミナルで「python manage.py init_db」と入力すると「entries」というテーブルが作られる
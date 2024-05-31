from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('flask_blog.config')

db = SQLAlchemy(app)  #dbという変数を参照することでDBを扱うことができるようになった

from flask_blog.views import views, entries
import os

DEBUG = True
SECRET_KEY = "todo-list@suzuki.sota.ok"
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(
    **{
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", "mysql"),
        "host": os.getenv("DB_HOST", "localhost"),
        "database": os.getenv("DB_DATABASE", "ENSHU")
    }
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
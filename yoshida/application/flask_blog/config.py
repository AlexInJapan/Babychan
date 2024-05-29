DEBUG = True
SECRET_KEY = "secret key"
USERNAME = "john"#〇！
PASSWORD = "due123"

#SQLARCHEMY_DATABASE_URI = "sqlite://flask_blog.db"
#SQLARCHEMY_TRACK_MODIFICATIONS = True

import os

SQLARCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(**{
    "user":os.getenv("DB_USER","root"),
    "password":os.getenv("DB_PASSWORD","mysql"),
    "host":os.getenv("DB_HOST","localhost"),
    "database":os.getenv("DB_DATABASE","ENSHU")
    })
SQLARCHEMY_TRACK_MODIFICATIONS = False
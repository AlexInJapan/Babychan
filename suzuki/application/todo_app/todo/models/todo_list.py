from todo import db

"""
todoListテーブル仕様
|項目名|データ型|PRIMARY KEY|備考|
|id|CHAR(8)|X|一意のタスクID|
|todo_name|VARCHAR(30)||タスク名|
|todo_date|DATE||タスク期日|
|todo_text|TEXT||タスク備考|
"""

class Todo(db.Model):
    __tablename__ = "todoList"
    id = db.Column(db.String(8), primary_key=True)
    todo_name = db.Column(db.String(30))
    todo_date = db.Column(db.Date)
    todo_text = db.Column(db.Text)

    def __init__(
            self, id=None, todo_name=None, 
            todo_date=None, todo_text=None):
        self.id = id
        self.todo_name = todo_name
        self.todo_date = todo_date
        self.todo_text = todo_text
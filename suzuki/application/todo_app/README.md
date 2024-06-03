# ToDoアプリ仕様
## 仕様メモ
- ログイン
- ログイン後トップページ表示
- トップページには、todoと新規作成、編集
    - 日付昇順で表示
    - できれば直近一週間以内にしぼって表示
    - なければ「タスクはありません」のような文章を表示
    - チェックボックスをつけて、一括削除とかできるようにしたい
- 新規作成ボタンを押すと、todo作成画面に遷移
- 一覧表示ボタンを押すと全てのタスクが表示
- todo作成画面でタスクの内容と日付を指定
## ディレクトリ構成
```
- todo-app/
|- server.py
|- manage.py
|- todo/
    |- ＿init＿.py
    |- config.py
    |- scripts/
    |   |- db.py
    |
    |- models/
    |   |- todo_list.py
    |
    |- views/
    |   |- ＿init＿.py
    |   |- views.py
    |   |- todo_backend/
    |       |- input.py
    |       |- confirm.py
    |       |- result.py
    |       |- list.py
    |
    |- templates/
        |- layout.html
        |- login.html
        |- todo_frontend/
            |- input.html
            |- confirm.html
            |- result.html
            |- list.html
```

## 開発手順
1. [x] 上記のファイルを空状態でいいので作成
2. [x] ＿init.py＿に初期化の処理を記述
3. [x] config.pyにバックエンド側の設定を記述
4. [x] todo_list.pyにtodoテーブルの定義を記述
5. [x] db.pyにスクリプトを実行する処理を記述
6. [x] manage.py スクリプトファイルをコンソール上で実行する処理を記述
7. [x] manage.pyを実行し、todoテーブルができているか確認
8. [x] server.pyにサーバーを立ち上げる処理を記述
9. [x] layout.htmlに共通部分のテンプレートを記述
10. [x] logim.htmlにログイン画面（フロントエンド）を記述
11. [x] views.pyにログインの処理（バックエンド）を記述
12. [x] input.htmlに入力画面（フロントエンド）を記述
    - [x] とりあえず見た目だけ作成
    - [x] formタグのパス
13. [x] input.pyに入力画面（バックエンド）の処理を記述
14. [x] result.pyにtodo追加処理（バックエンド）を記述
15. [ ] list.htmlに一覧参照画面（フロントエンド）を記述
16. [ ] list.pyに一覧参照処理（バックエンド）を記述

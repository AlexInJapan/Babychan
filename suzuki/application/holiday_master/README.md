# 祝日マスター仕様
## ディレクトリ構成
```
- holiday_master/
|- server.py
|- holiday/
   |- __init__.py
   |- config.py
   |- views/
   |  |- __init__.py
   |  |- input.py
   |  |- maintenance_date.py
   |  |- list.py
   |- models/
   |  |- mst_holiday.py
   |- templates/
      |- layout.html
      |- input.html
      |- result.html
      |- list.html
```
 ## 開発手順
1. [x] 上記のファイルを空状態でいいので全て作る
2. [x] ＿init＿.pyに初期化の処理を記述
3. [x] config.pyにバックエンド側の設定を記述
4. [x] server.pyにサーバーを立ち上げる処理を記述
5. [x] layout.htmlに共通部分のテンプレートを記述
6. [x] mst_holiday.pyに祝日テーブルの定義を記述
7. [x] input.htmlに入力画面（フロントエンド）を記述
8. [ ] input.pyに入力画面（バックエンド）の処理を記述
9. [ ] result.htmlに結果画面（フロントエンド）を記述
10. [ ] maintenance_date.pyに結果画面（バックエンド）の処理を記述
11. [ ] list.htmlに一覧画面（フロントエンド）を記述
12. [ ] list.pyに一覧画面（バックエンド）の処理を記述
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
8. [x] input.pyに入力画面（バックエンド）の処理を記述
9. [x] result.htmlに結果画面（フロントエンド）を記述
10. [x] maintenance_date.pyに結果画面（バックエンド）の処理を記述
11. [x] list.htmlに一覧画面（フロントエンド）を記述
12. [x] list.pyに一覧画面（バックエンド）の処理を記述

## 機能ごとに要件を整理
### 入力画面
- [x] 祝日日付入力ボックス
- [x] 祝日テキスト入力ボックス
- [x] 新規登録・更新ボタン
- [x] 削除ボタン
- [x] 一覧出力ボタン
### 結果画面
- [x] 処理結果（テキスト）
   - [x] 新規登録
   - [x] 更新
   - [x] 削除
- [x] 入力画面に戻るボタン
### 一覧照会画面
- [x] 表見出し
- [x] 祝日マスタを列ごとに一覧表示
- [x] 入力画面に戻るボタン

## バリデーション
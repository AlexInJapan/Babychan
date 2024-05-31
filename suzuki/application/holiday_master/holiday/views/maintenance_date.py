from flask import (
    request, 
    redirect, 
    url_for, 
    render_template, 
    flash, 
    session)
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday
from datetime import datetime

# input.pyから日付と祝日名を受け取り、新規登録・更新する
@app.route('/maintenance_date', methods=['POST', 'GET'])
def update_holiday():

    # 入力画面から祝日日付を取得
    holiday_date = request.form['holiday']
    holiday_date = datetime.strptime(holiday_date, "%Y-%m-%d").date()

    # 入力画面から祝日名を取得
    holiday_text = request.form['holiday_text']

    # 入力値をHolidayインスタンスに代入
    holi_dict = Holiday(
                holi_date=holiday_date,
                holi_text=holiday_text)

    # メッセージIDを格納する変数を宣言
    msg_id = ""

    # 祝日テーブルから入力に対応する列を取得
    holiday = Holiday.query.get(holiday_date)

    # 祝日テーブルに入力した日付がない場合
    if holiday is None:
        if request.form["button"] == "insert_update":
            new_holiday = holi_dict
            db.session.add(new_holiday)
            db.session.commit()
            msg_id = "IO1"
        elif request.form["button"] == "delete":
            flash(f"{holiday_date}は、祝日マスタに登録されていません")
            return redirect('/')

    # 祝日テーブルに入力した日付がある場合
    elif holiday.holi_date == holiday_date:
        # 更新処理
        if request.form["button"] == "insert_update":
            update_holiday = holi_dict
            db.session.merge(update_holiday)
            db.session.commit()
            msg_id = "IO2"
        # 削除処理
        elif request.form["button"] == "delete":
            db.session.delete(holiday)
            db.session.commit()
            msg_id = "IO3"

    # 祝日マスタが登録されていない場合
    else:
        msg_id = "IO4"

    return render_template(
            "result.html",
            holiday_date=holiday_date,
            holiday_text=holiday_text,
            msg_id = msg_id
        )


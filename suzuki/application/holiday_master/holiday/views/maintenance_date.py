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
    holiday_date = request.form['holiday']
    holiday_date = datetime.strptime(holiday_date, "%Y-%m-%d").date()
    holiday_text = request.form['holiday_text']
    msg_id = ""    
    # 入力した祝日が、テーブルに存在するか確認
    holiday = Holiday.query.get(holiday_date)
    if holiday is None:
        new_holiday = Holiday(
            holi_date=holiday_date,
            holi_text=holiday_text
        )
        db.session.add(new_holiday)
        db.session.commit()
        msg_id = "IO1"
    elif holiday.holi_date == holiday_date:
        update_holiday = Holiday(
            holi_date=holiday_date,
            holi_text=holiday_text
        )
        db.session.merge(update_holiday)
        db.session.commit()
        msg_id = "IO2"
    else:
        flash('エラーが起きました。もう一度やり直してください')
        return redirect('/')
    return render_template(
            "result.html",
            holiday_date=holiday_date,
            holiday_text=holiday_text,
            msg_id = msg_id
        )


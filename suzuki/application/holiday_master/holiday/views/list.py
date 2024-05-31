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

@app.route('/list', methods=['POST', 'GET'])
def show_holidays():
    holidays = Holiday.query.order_by(Holiday.holi_date.desc()).all()
    return render_template("list.html", holidays=holidays)
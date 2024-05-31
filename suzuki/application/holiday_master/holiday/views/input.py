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

# 入力画面
@app.route('/')
def input():
    return render_template('input.html')
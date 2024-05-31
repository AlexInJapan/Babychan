from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP

@app.route('/', methods=['GET','POST'])
def input():
    input_data = session.get('input_data',None)
    return render_template("input.html", input = input_data)

@app.route('/output', methods=['GET','POST'])  
def output():
    session["input_data"] = request.form["salary"]

    #バリデーション
    if request.form["salary"] == "":
        flash("給与が未入力です。入力してください。")
        return redirect('/')
    elif len(request.form["salary"]) > 10:
        flash("給与には最大9,999,999,999まで入力可能です")
        return redirect('/')
    elif int(request.form["salary"]) < 0:
        flash("給与にはマイナスの値は入力できません")
        return redirect('/')  

    #計算
    if request.method == 'POST':
        #引数を変数に代入
        salary = int(request.form["salary"])
        # 税額の計算
        if salary <= 1000000:
            tax = salary * 0.1
        else:
            salary_plus = salary - 1000000
            tax = (salary_plus * 0.2) + (1000000 * 0.1)
        tax = Decimal(tax).quantize(Decimal("0"), rounding = ROUND_HALF_UP)
        # 支給額の計算
        pay = salary - tax
    return render_template('output.html', salary=salary, pay=pay, tax=tax)
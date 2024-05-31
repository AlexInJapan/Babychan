from flask import request, redirect, url_for, render_template, flash, session
from salary import app

# 給与を計算する関数を定義
def calc_salary(input_salary):
    if (input_salary > 1000000):
        # 100万円を超過した部分を取り出す
        over_milion = input_salary - 1000000
        # 税額の計算
        tax = over_milion * 0.2 + 100000
    else:
        # 税額の計算
        tax = input_salary * 0.1
    tax = round(tax)
    payment = input_salary - tax

    salary = "{:,}".format(input_salary)
    payment = "{:,}".format(payment)
    tax = "{:,}".format(tax)
    return salary, payment, tax

@app.route("/")
def top():
    return render_template("input.html")

#給与が未入力の場合を定義
@app.route("/")
def not_entered()
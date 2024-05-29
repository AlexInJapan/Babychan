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

@app.route("/output" , methods=["GET", "POST"])
def show_result():
    error = None
    if request.method == "POST":
        input_salary = request.form["salary"]
        if input_salary == "":
            flash("給与が未入力です。入力してください。")
            return redirect("/")
        input_salary = int(input_salary)

        if input_salary >= 10000000000:
            flash("給与には最大9,999,999,999まで入力可能です")
            return redirect("/")
        if input_salary < 0:
            flash("給与にはマイナスの値は入力できません。")
            return redirect("/")
        salary, payment, tax = calc_salary(input_salary)
    return render_template(
        "output.html",
        salary=salary,
        payment=payment, 
        tax=tax)

"""
@app.route("/", methods=["GET", "POST"])
def input():
    input_data = session.get("input_data", None)
    return render_template("input.html", input = input_data)

def output():
    session["input_data"] = ""
    # バリデーション処理

"""
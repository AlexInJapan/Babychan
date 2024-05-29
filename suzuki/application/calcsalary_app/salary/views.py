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


@app.route("/", methods=["GET", "POST"])
def input():
    # sessionから前回の入力情報があれば取得する
    input_data = session.get("input_data", None)

    # input.htmlにテンプレートおよび前回の入力情報を返す
    return render_template("input.html", input = input_data)


@app.route("/output" , methods=["GET", "POST"])
def output():
    error = None

    # input.htmlで入力した値をsessionに保存する
    session["input_data"] = request.form["salary"]

    # リクエストがPOSTのとき、給与計算をする
    if request.method == "POST":

        # 入力が空の場合は受け付けない      
        if session["input_data"] == "":
            flash("給与が未入力です。入力してください。")
            return redirect("/")

        # 入力値を文字列型から整数型に変換する
        input_salary = int(session["input_data"])

        # 10000000000以上の入力は受け付けない
        if input_salary >= 10000000000:
            flash("給与には最大9,999,999,999まで入力可能です")
            return redirect("/")
        
        # 負の値も受け付けない
        if input_salary < 0:
            flash("給与にはマイナスの値は入力できません。")
            return redirect("/")

        # calc_salary関数で給与計算をする
        salary, payment, tax = calc_salary(input_salary)

    # output.htmlにテンプレートおよび計算結果を返す
    return render_template(
        "output.html",
        salary=salary,
        payment=payment, 
        tax=tax)

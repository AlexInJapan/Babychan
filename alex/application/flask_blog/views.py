from flask import request,redirect,url_for, render_template, flash, session
from flask_blog import app

SALARY_MAX =1000000
SALARY_TAX_10 = 0.1
SALARY_TAX_20 = 0.2
def SentBackToLoginPage():
    if not session.get("logged_in"):
      return redirect("/login")      

def SalaryToTaxedSalary(salary):

    salary = int(salary)
    if salary >SALARY_MAX:
        taxed_salary = round(SALARY_TAX_10*SALARY_TAX_10 + (salary-SALARY_MAX)*SALARY_TAX_20)
    else:
        taxed_salary = round(salary*SALARY_TAX_10)
    
    
    return [salary,salary-taxed_salary,taxed_salary]

@app.route("/")
def show_entries():
    SentBackToLoginPage()
    return render_template("entries/index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method =="POST":
        if request.form["username"]!=app.config["USERNAME"]:
            flash("Incorrect username")
        elif request.form["password"]!=app.config["PASSWORD"]:
            flash("Incorrect password")
        else:
            session["logged_in"] = True
            flash("Logged In")
            return redirect("/")
    return render_template("login.html")

@app.route("/input")
def SalaryInput():
    SentBackToLoginPage()
    return render_template("input.html")


@app.route("/output", methods=["POST"])
def CalcSalary():
    if request.method == "POST":
        SentBackToLoginPage()
        userInputSalary = request.form["salary"]
        if userInputSalary == "" or int(userInputSalary)==0:
            flash("Enter correct value")
            return render_template("input.html")
        else:
            salary_detail = SalaryToTaxedSalary(userInputSalary)
            return render_template("output.html", salary_detail=salary_detail)
        
    

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect("/")

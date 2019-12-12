import logging

from flask import Flask, render_template, request, session, redirect, url_for, send_file

app = Flask(__name__)
app.secret_key = "password"
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run(debug=True, host='0.0.0.0')

@app.route("/", methods = ["GET", "POST"])
def intropage():
    if request.method == "POST":
        session['firstName'] = request.form['firstName']
        session['lastName'] = request.form['lastName']
        return redirect(url_for('page1'))
    elif request.method == "GET":
        return render_template("intropage.html")

@app.route("/choicepage")
def choicepage():
    return render_template("choicepage.html", firstName = session['firstName'], lastName=session['lastName'])

@app.route("/page1",  methods = ["GET", "POST"])
def page1():
    if request.method == "POST":
        return render_template("choicepage.html", firstName = session['firstName'], lastName=session['lastName'])
    elif request.method == "GET":
        return render_template("page1.html", firstName = session['firstName'], lastName=session['lastName'])

@app.route("/page2",  methods = ["GET", "POST"])
def page2():
    if request.method == "POST":
        return render_template("choicepage.html", firstName = session['firstName'], lastName=session['lastName'])
    elif request.method == "GET":
        return render_template("page2.html", firstName = session['firstName'], lastName=session['lastName'])

@app.route("/page3",  methods = ["GET", "POST"])
def page3():
    if request.method == "POST":
        return render_template("page3.html", firstName = session['firstName'], lastName=session['lastName'])
    elif request.method == "GET":
        return render_template("page3.html", firstName = session['firstName'], lastName=session['lastName'])

@app.route("/page4",  methods = ["GET", "POST"])
def page4():
    if request.method == "POST":
        return render_template("page4.html", firstName = session['firstName'], lastName=session['lastName'])
    elif request.method == "GET":
        return render_template("page4.html", firstName = session['firstName'], lastName=session['lastName'])

@app.route("/page5",  methods = ["GET", "POST"])
def page5():
    if request.method == "POST":
        return render_template("page5.html", firstName = session['firstName'], lastName=session['lastName'])
    elif request.method == "GET":
        return render_template("page5.html", firstName = session['firstName'], lastName=session['lastName'])

@app.route("/page6",  methods = ["GET", "POST"])
def page6():
    if request.method == "POST":
        return render_template("page6.html", firstName = session['firstName'], lastName=session['lastName'])
    elif request.method == "GET":
        return render_template("page6.html", firstName = session['firstName'], lastName=session['lastName'])

@app.route("/page7",  methods = ["GET", "POST"])
def page7():
    if request.method == "POST":
        session['userresponse'] = request.form['userresponse']
        return render_template("page9.html", firstName = session['firstName'], lastName=session['lastName'], response = session['userresponse'])
    elif request.method == "GET":
        return render_template("page7.html", firstName = session['firstName'], lastName=session['lastName'])

@app.route("/page8",  methods = ["GET", "POST"])
def page8():
    if request.method == "POST":
        return render_template("page8.html", firstName=session['firstName'], lastName=session['lastName'])
    elif request.method == "GET":
        return render_template("page8.html", firstName = session['firstName'], lastName=session['lastName'])

@app.route("/page9",  methods = ["GET", "POST"])
def page9():
    return render_template("choicepage.html", firstName = session['firstName'], lastName=session['lastName'], response = session['userresponse'])
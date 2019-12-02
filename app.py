import logging

from flask import Flask, render_template, request, session, redirect, url_for, send_file

app = Flask(__name__)
app.secret_key = "password"
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run(debug=True, host='0.0.0.0')

@app.route("/", methods = ["GET", "POST"])
def startpage():
    if request.method == "POST":
        session['firstName'] = request.form['firstName']
        session['lastName'] = request.form['lastName']
        return redirect(url_for('page1'))
    elif request.method == "GET":
        return render_template("startpage.html")

@app.route("/page1")
def page1():
    return render_template("page1.html", lastName=session['lastName'])


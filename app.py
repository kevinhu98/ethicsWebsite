import logging

from flask import Flask, render_template, request, session, redirect, url_for, send_file



app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run(debug=True, host='0.0.0.0')


@app.route("/")
def startpage():
    return render_template("startpage.html")


    
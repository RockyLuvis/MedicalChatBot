from flask import flask, render_template

app = flask(__name__)

@app.route("/")
def home_page():
    return render_template("chat.html")

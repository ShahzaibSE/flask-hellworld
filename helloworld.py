from flask import Flask, render_template

app = Flask(__name__)
app.testing = True

@app.route("/")
def helloworld() :
    return '<h1>Hello World</h1>'

@app.route("/welcome")
def welcomePage():
    return render_template("welcome.html")    
from flask import Flask
from flask import render_template, request, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/", methods = ["GET","POST"])
def index():
    if(request.method == "POST"):
        return render_template("finding.html")
    else:
        return render_template("index.html")
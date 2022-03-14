from flask import Flask
from flask import render_template, request, redirect
from flask_bootstrap import Bootstrap
import re

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/", methods = ["GET","POST"])
def index():
    if(request.method == "POST"):
        url = request.form.get("url")

        # URLチェック
        pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
        if re.match(pattern, url):
            print("Is URL:" + url)
            return render_template("finding.html",url=url)
        else:  
            print("Not URL:" + url)
            return redirect("/")
    else:
        return render_template("index.html")
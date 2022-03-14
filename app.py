from flask import Flask, make_response
from flask import render_template, request, redirect
from flask_bootstrap import Bootstrap
import datetime
import re

import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/", methods = ["GET","POST"])
def index():
    if(request.method == "POST"):
        url = request.form.get("url")

        # URLチェック
        pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
        if re.match(pattern, url):
            # 時間取得
            t_delta = datetime.timedelta(hours=9)
            JST = datetime.timezone(t_delta, 'JST')
            now = datetime.datetime.now(JST)
            time = now.strftime("%Y%m%d")

            # 画像取得
            response = requests.get(url)
            soup = BeautifulSoup(response.text,'lxml')
            allImages = soup.findAll("img")
            images = []
            for image in allImages:
                if(image["src"].startswith("http")):
                    images.append(image["src"])

            return render_template("result.html",url=url ,images = images ,imgLen = len(images))
        else:  
            return render_template("error.html",errorText="正しいURLを入力してください。")
    else:
        return render_template("index.html")
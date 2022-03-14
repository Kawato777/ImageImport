from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!!"
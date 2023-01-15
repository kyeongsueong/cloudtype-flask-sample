from flask import Flask, request, redirect, render_template, url_for, Response

app = Flask(__name__)

@app.route("/")
def index():
    getDatas = "hihi"
    photo = f"/img/1.jpeg"
    return render_template('./index.html', getDatas=getDatas, photo=photo)

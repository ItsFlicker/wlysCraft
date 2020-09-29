from flask import render_template, request, url_for, redirect
from wlysCraft import app


@app.route('/')
def main():
    return redirect('/index')

@app.route('/index/')
def index():
    return render_template("index.html")

@app.route('/programs/')
def programs():
    return render_template("programs.html")

@app.route('/download/')
def download():
    return render_template("download.html")

@app.route('/video/')
def video():
    return render_template("video.html")
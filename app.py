"""
app.py

Flask on Herouku web app example
Jeremy Smith

Cloned from https://github.com/thedataincubator/flask-framework
Modified 8/18/2017

"""

import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 33507))
    app.run(port=port)

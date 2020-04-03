from app import app
from flask import render_template, url_for, request

@app.route('/')
def home():
    return render_template('home.html')
    
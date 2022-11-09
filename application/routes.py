from flask import render_template, request

from application import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/carmatch')
def carmnatch():
    return render_template('carmatch.html', title="Car Match")

# @app.route('/carmatch')
# def carmnatch():
#     return render_template('carmatch.html', title="Car Match")

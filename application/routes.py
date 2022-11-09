from flask import render_template

from application import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/carmatch')
def carmatch():
    return render_template('carmatch.html', title="Matcher")

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html', title="Subscribe")

@app.route('/showroom')
def showroom():
    return render_template('showroom.html', title="Showroom")
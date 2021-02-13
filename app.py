from flask import flask, render

@app.route('/')
def home():
    return render_template('home.html')

app.route('/results')
def home():
    return render_template('results.html')
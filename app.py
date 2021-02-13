from flask import flask, render

@app.route('/')
def home():
    return render_template('index.html')
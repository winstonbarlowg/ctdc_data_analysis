from flask import (
    Blueprint, Flask, flash, g, redirect, render_template, request, url_for
)

app = Flask(__name__)

# app = Blueprint('website', __name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/maps')
def maps():
    return render_template('mapsclustering.html')

if __name__ == '__main__':
    app.run(debug=True)

    
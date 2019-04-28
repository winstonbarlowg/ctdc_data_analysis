from flask import (
    Blueprint, Flask, flash, g, redirect, render_template, request, url_for, make_response, current_app, send_from_directory
)
# from projecth import *
# from projecth.dashapp import app
app = Flask(__name__)
# app = Blueprint('website', __name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('main.html')

@app.route('/maps', methods=['GET', 'POST'])
def maps():
    return render_template('mapsclustering.html')

@app.route('/about')
def about():
    return render_template('about.html')

# return geojson file for Google Maps API clustering
# send_from_ directory is a secure way to expose static files
@app.route('/data/<path:themap>')
def data_for_map(themap):
    return send_from_directory('static', 'themap_GeoJSON.js')

@app.route('/gender')
def scatter():
    return render_template('gender_breakdown.html')

# run app in debug mode, running the script directly to save time
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port =80, debug=True)

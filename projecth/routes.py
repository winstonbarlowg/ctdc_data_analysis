from flask import (
    Blueprint, Flask, flash, g, redirect, render_template, request, url_for, make_response, current_app
)

from app import *
from app.dashapp import app
# app = Flask(__name__)
# app = Blueprint('website', __name__)

@server.route('/')
def index():
    return render_template('main.html')

@server.route('/maps', methods=['GET', 'POST'])
def maps():
    return render_template('mapsclustering.html')

@server.route('/about')
def about():
    return render_template('about.html')

# return geojson file for Google Maps API clustering
@server.route('/data/map_data')
def data_for_map():
    return server.send_static_file('themap.json')

@server.route('/scatter')
def scatter():
    return render_template('scatter.html')

# run app in debug mode, running the script directly to save time
# if __name__ == '__main__':
#     app.run(debug=True)

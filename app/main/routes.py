from flask import (
    Blueprint, Flask, flash, g, redirect, render_template, request, url_for, current_app
)

main = Blueprint('main', __name__,)

# template_folder='templates'

@main.route('/')
def index():
    return render_template('main.html')

@main.route('/maps', methods=['GET', 'POST'])
def maps():
    return render_template('mapsclustering.html')

@main.route('/about')
def about():
    return render_template('about.html')

# return geojson file for Google Maps API
# @main.route('/data/map_data')
# def data_for_map():
#     return app.send_static_file('themap.json')

@main.route('/scatter')
def scatter():
    return render_template('scatter.html')

# run app in debug mode, running the script directly to save time
# if __name__ == '__main__':
#     app.run(debug=True)








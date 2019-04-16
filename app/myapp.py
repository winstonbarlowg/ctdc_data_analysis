from flask import (
    Blueprint, Flask, flash, g, redirect, render_template, request, url_for, make_response, current_app
)

app = Flask(__name__)

# app = Blueprint('website', __name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/maps', methods=['GET', 'POST'])
def maps():
    return render_template('mapsclustering.html')

@app.route('/about')
def about():
    return render_template('about.html')

# return geojson file for Google Maps API
@app.route('/data/map_data')
def data_for_map():
    return app.send_static_file('themap.json')

@app.route('/scatter')
def scatter():
    return render_template('scatter.html')

# run app in debug mode, running the script directly to save time
if __name__ == '__main__':
    app.run(debug=True)







'''
If the source file is executed as the main program, 
the interpreter sets the __name__ variable to have a value “__main__”. 
If this file is being imported from another module, __name__ will be set to the module’s name.
'''
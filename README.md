# About this project

Project H is my final project for a SWE course, putting together what I learned and building a website that shows impactful data about a delicate issue: Human Trafficking.

The dataset used can be found here: https://www.ctdatacollaborative.org/

### Technologies used

- Python + Pandas for data analysis
- Python + Flask for backend
- Chart.js for visualisations
- HTML + CSS (Bootstrap)
- Google Maps API

## Installation

- Clone this repository
- Create an environment:
```
cd SE_Foundations_Project
python3 -m venv venv
```
- Activate the environment and install the requirements:
```
. venv/bin/activate
pip install -r requirements.txt
```

## Usage

- `cd projecth` to run the server locally.
Make sure that the last block looks like this:
```python
if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port =80, debug=True)
```
The last line shall be commented out when running it locally as it is meant for Google Cloud.
- Start the server with `python routes.py` and then go to http://localhost:5000 to see the website running.

## Data

- Firstly, the global dataset must be downloaded from: https://www.ctdatacollaborative.org/download-global-dataset as CSV and saved in the `resources` directory.

- `dataexports.py` can be used to look into some subsets of the global datasets easily through the REPL by calling specific variables or creating new ones.

- To work with a Jupyter notebook, just run `jupyter notebook` in the main directory of the project with the enviroment activated. 

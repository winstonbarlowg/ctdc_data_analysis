# SE Foundations Semester @ CODE University
Final project for software engineering course.

## Technologies used
- Python + Pandas for data analysis
- Python + Flask for backend
- Chart.js for visualisations
- HTML + CSS (Bootstrap)
- Google Maps API

## Running the App
- Clone this repository
- Create virtual environment:
```
cd SE_Foundations_Project
python3 -m venv venv
```
- Start virtual environment and install requirements:
```
. venv/bin/activate
pip install -r requirements.txt
```
- cd projecth/ to run server routes.py locally.
Make sure that the last block looks like this:
```python
if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port =80, debug=True)
```
- Start the server with `python routes.py` and go to localhost:5000

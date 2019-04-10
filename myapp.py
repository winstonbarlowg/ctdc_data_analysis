from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

app = Blueprint('website', __name__)

@app.route('/')
def index():
    
from flask import Flask

app = Flask(__name__)

from projecth.routes import *

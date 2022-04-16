from distutils.log import debug
from flask import Flask


app = Flask(__name__)

@app.get("/")
def index():

    me = {
        "first": "Phil",
        "last": "Chaplin",
        "hobbies": "Scuba Diving",
    }
    return me


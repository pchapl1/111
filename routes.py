from distutils.log import debug
from flask import Flask


app = Flask(__name__)

@app.get("/aboutme")
def index():

    me = {
        "first_name": "Phil",
        "last_name": "Chaplin",
        "hobby": "Scuba Diving",
    }
    return me


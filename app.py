from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/home')
def index():
    return "Hello Flask"

@app.route('/users/<user_id>', methods=["GET", "POST", "PUT", "DELETE"])
def parameter(user_id):
    if request.method == "GET":
        return "GET method"


    if request.method == "POST":
        data = request.form
        return data

    if request.method == "PUT":
        return "PUT method"

    if request.method == "DELETE":
        return "DELETE method"
    else:
        "Not allowed method"

app.run() # (host="localhost", port=81)


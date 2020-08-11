import os
import json

# Import the flask class
from flask import Flask, render_template

# Create an instance of this class
# Convention is that the variable be called app

"""
The first argument
of the Flask class is the name of the applications module - our package. Since
we're just using a single module, we can use __name__
which is a built-in Python variable. Flask needs
this so that it knows where to look for templates and static files.
"""
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    # initialise epty list data variable
    data = []
    # open the .json file as read only, and assigning contents to json_data
    with open("data/company.json", "r") as json_data:
        # the data list will be equal to the json data
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == '__main__':
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

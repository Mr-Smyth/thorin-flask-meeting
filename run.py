import os

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

# Use route decorator to tell Flask what url should trigger the function that follows
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
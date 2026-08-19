from flask import render_template
# Import the `render_template` function to render HTML templates.

from app import app
# Import the Flask application instance (`app`) from the `app` package.

@app.route("/")
def home():
    # Define the route for the home page (`/`).
    # When the user visits the root URL, the `home.html` template is rendered.
    return render_template("home.html")

@app.route("/about")
def about():
    # Define the route for the about page (`/about`).
    # When the user visits `/about`, the `about.html` template is rendered.
    return render_template("about.html")

@app.route("/contact")
def contact():
    # Define the route for the contact page (`/contact`).
    # When the user visits `/contact`, the `contact.html` template is rendered.
    return render_template("contact.html")
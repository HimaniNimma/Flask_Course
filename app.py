from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return "This is the about page of my Flask application."
app.run(debug=True)
from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def home():
    name = "Himani"
    course="Flask"
    age=21
    is_student=True
    skills = ["Python", "Flask", "HTML", "CSS"]
    return render_template(
        "index.html",
        name=name,
        age=age,
        course=course,
        is_student=is_student,
        skills=skills
    )
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
app.run(debug=True)
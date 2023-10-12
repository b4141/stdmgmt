from flask import render_template, flash, redirect, url_for
from stdmgmt import app, db
from stdmgmt.forms import StudentRegistrationForm
from stdmgmt.models import Student

@app.route("/")
def index():
    return render_template('index.html', title="home page")

@app.route("/addStudent", methods=['GET', 'POST'])
def addStudent():
    form = StudentRegistrationForm()
    if form.validate_on_submit():
        flash("Successfully added a new Student", "success")
        print(form.data)
        return redirect(url_for('index'))
    return render_template('addStudent.html', title="Student registration", form=form)

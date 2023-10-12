from flask import Flask, render_template, flash, redirect, url_for
from forms import StudentRegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

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

if __name__ == "__main__":
    app.run(debug=True)

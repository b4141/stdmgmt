import secrets
import os
from flask import render_template, flash, redirect, url_for
from stdmgmt import app, db
from stdmgmt.forms import StudentRegistrationForm
from stdmgmt.models import Student

def saveStudentPicture(formPicture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(formPicture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/studentPics', picture_fn)
    formPicture.save(picture_path)
    return picture_fn


@app.route("/")
def index():
    # flash("Successfully added a new Student", "success")
    # flash("Successfully added a new Student", "error")
    return render_template('index.html', title="home page")

@app.route("/studentProfile/<studentNumber>")
def studentProfile(studentNumber):
    try:
        student = Student.query.filter(Student.registrationNumber == str(studentNumber)).first()
        # return f"{student.registrationNumber}, {student.picture}"
        return render_template('studentProfile.html', title="student profile", student=student)
    except:
        return "student does not exist"

@app.route("/addStudent", methods=['GET', 'POST'])
def addStudent():
    form = StudentRegistrationForm()
    if form.validate_on_submit():
        try:
            try:
                if Student.query.filter(Student.registrationNumber == str(form.registrationNumber.data)).first():
                    flash(f'the registration number "{form.registrationNumber.data}" already exists', "error")
                    return redirect(url_for('index'))
            except:
                pass
                
            student = Student(
                registrationNumber = form.registrationNumber.data,
                picture = saveStudentPicture(form.picture.data),
                frenchLastName = form.frenchLastName.data,
                frenchFirstName = form.frenchFirstName.data,
                arabicLastName = form.arabicLastName.data,
                arabicFirstName = form.arabicFirstName.data,
                grade = form.grade.data,
                nationality = form.nationality.data,
                bloodGroup = form.bloodGroup.data,
                birthDate = form.birthDate.data,
                birthPlace = form.birthPlace.data,
                fatherName = form.fatherName.data,
                fatherProfession = form.fatherProfession.data,
                motherName = form.motherName.data,
                motherProfession = form.motherProfession.data,
                address = form.address.data,
                parentsDivorced = form.parentsDivorced.data,
                fatherDead = form.fatherDead.data,
                fatherDeathDate = form.fatherDeathDate.data,
                motherDead = form.motherDead.data,
                motherDeathDate = form.motherDeathDate.data,
                siblingsNumber = form.siblingsNumber.data,
                joiningDate = form.joiningDate.data,
                arrivalDate = form.arrivalDate.data,
                departureDate = form.departureDate.data,
                phoneNumber = form.phoneNumber.data,
                parentPhoneNumber = form.parentPhoneNumber.data)
            db.session.add(student)
            db.session.commit()
            flash("Successfully added a new Student", "success")
        except:
            flash(f"there was an error, try again, you probably got something wrong", "error")
            
        return redirect(url_for('index'))

    return render_template('addStudent.html', title="Student registration", form=form)

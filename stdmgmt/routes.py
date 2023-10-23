import os
from flask import render_template, flash, redirect, url_for, request
from stdmgmt import app, db
from stdmgmt.forms import StudentRegistrationForm, StudentModifyForm
from stdmgmt.models import Student
from stdmgmt.utils import *



@app.route("/")
def index():
    return render_template('index.html', title="home page")


@app.route("/studentProfile/<studentNumber>")
def studentProfile(studentNumber):
    student = Student.query.filter(Student.registrationNumber == str(studentNumber)).first()
    return render_template('studentProfile.html', title="student profile", student=student)


@app.route("/deleteStudent", methods=['GET', 'POST'])
def deleteStudent():
    if request.method == 'POST':
        postJsonData = request.get_json()
        if postJsonData["action"] == "deleteStudent":
            student = Student.query.filter(Student.id == postJsonData["studentId"]).first()
            if (postJsonData["studentId"] == student.id) and (postJsonData["studentRegistrationNumber"] == student.registrationNumber):
                #__need_to_do_some_cleaning_like_delete_the_picture
                db.session.delete(student)
                db.session.commit()
            
    return render_template('index.html', title="home page")



@app.route("/modifyStudent/<studentNumber>", methods=['GET', 'POST'])
def modifyStudent(studentNumber):
    student = Student.query.filter(Student.registrationNumber == str(studentNumber)).first()
    form = StudentModifyForm()

    if form.validate_on_submit():

        student = Student.query.filter(Student.id == student.id).first()
        student = reassignStudentInfo(student, form)
        #__put_the_code_here
        if form.data['picture'] != None:
            print("----", student.picture)
            print("----", form.picture.data)
            _ = saveStudentPicture(form.picture.data, student.picture)
           
        db.session.commit()
        return redirect(url_for('index'))

    if student != None:
        form = fillForm(form, student)
    # print("image :", student.picture)
    return render_template('modifyStudent.html', title="Student registration", form=form, student=student)



@app.route("/addStudent", methods=['GET', 'POST'])
def addStudent():
    form = StudentRegistrationForm()
    if form.validate_on_submit():
        try:
            if Student.query.filter(Student.registrationNumber == str(form.registrationNumber.data)).first():
                print("student exists")
                flash(f'the registration number "{form.registrationNumber.data}" already exists', "error")
                return redirect(url_for('index'))
                
            student = createStudent(form)
            db.session.add(student)
            db.session.commit()
            flash("Successfully added a new Student", "success")
        except:
            flash(f"there was an error, try again, you probably got something wrong", "error")
            
        return redirect(url_for('index'))

    return render_template('addStudent.html', title="Student registration", form=form)

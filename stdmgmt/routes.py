import os
from flask import render_template, flash, redirect, url_for, request, jsonify, session
from stdmgmt import app, db
from stdmgmt.forms import StudentRegistrationForm, StudentModifyForm, adminLoginForm
from stdmgmt.models import Student
from stdmgmt.utils import *



@app.route("/login/", methods=['GET', 'POST'])
def login():
    if not isNotLoggedIn(session):
        print(isNotLoggedIn(session))
        return redirect(url_for('index'))

    form = adminLoginForm()
    if form.validate_on_submit():
        if form.data['password'] == getPassword():
            session['admin'] = 'admin'
            flash('loged in', 'success')
            return redirect(url_for('index'))
        else:
            flash('loged in', 'error')
            return redirect(url_for('login'))
        
    return render_template('login.html', title="loginPage page", form=form)


@app.route("/logout")
def logout():
    if isNotLoggedIn(session):
        return redirect(url_for('login'))
    else:
        session['admin'] = 'bob'
        return redirect(url_for('login'))
    return render_template('index.html', title="home page")

@app.route("/")
def index():
    if isNotLoggedIn(session):
        return redirect(url_for('login'))

    return render_template('index.html', title="home page")


@app.route("/studentProfile/<studentNumber>")
def studentProfile(studentNumber):
    if isNotLoggedIn(session):
        return redirect(url_for('login'))

    student = Student.query.filter(Student.registrationNumber == str(studentNumber)).first()
    return render_template('studentProfile.html', title="student profile", student=student)


@app.route("/deleteStudent", methods=['GET', 'POST'])
def deleteStudent():
    if isNotLoggedIn(session):
        return redirect(url_for('login'))

    if request.method == 'POST':
        postJsonData = request.get_json()
        if postJsonData["action"] == "deleteStudent":
            student = Student.query.filter(Student.id == postJsonData["studentId"]).first()
            if (postJsonData["studentId"] == student.id) and (postJsonData["studentRegistrationNumber"] == student.registrationNumber):
                deletPicture(student.picture)
                db.session.delete(student)
                db.session.commit()
                flash("تم حذف الطالب بنجاح", "success")
                return jsonify("success")
            else:
                flash("هناك خطأ ما", "error")
                return jsonify("success")
            
    return render_template('index.html', title="home page")



@app.route("/modifyStudent/<studentNumber>", methods=['GET', 'POST'])
def modifyStudent(studentNumber):
    if isNotLoggedIn(session):
        return redirect(url_for('login'))

    student = Student.query.filter(Student.registrationNumber == str(studentNumber)).first()
    form = StudentModifyForm()
    if student == None:
        flash("لا يوجد طالب بالمعرف السابق", "error")
        return redirect(url_for('index'))

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
    if isNotLoggedIn(session):
        return redirect(url_for('login'))

    form = StudentRegistrationForm()
    if form.validate_on_submit():
        try:
            if Student.query.filter(Student.registrationNumber == str(form.registrationNumber.data)).first():
                print("student exists")
                flash(f'رقم التسجيل ( {form.registrationNumber.data} ) موجود بالفعل', "error")
                return redirect(url_for('index'))
                
            student = createStudent(form)
            db.session.add(student)
            db.session.commit()
            flash("تمت إضافة طالب جديد بنجاح", "success")
        except:
            flash(f"حدث خطأ، حاول مرة أخرى، ربما حدث خطأ ما", "error")
            
        return redirect(url_for('index'))

    return render_template('addStudent.html', title="Student registration", form=form)

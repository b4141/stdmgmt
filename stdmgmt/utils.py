import secrets
from stdmgmt import app
from stdmgmt.models import Student
import os

def saveStudentPicture(formPicture, pictureName):
    if pictureName != None:
        print("name provided")
        picture_path = os.path.join(app.root_path, 'static/studentPics', pictureName)
        formPicture.save(picture_path)
        return pictureName

    print("name not provided")
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(formPicture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/studentPics', picture_fn)
    formPicture.save(picture_path)
    return picture_fn

def deletPicture(pictureName):
    picture_path = os.path.join(app.root_path, 'static/studentPics', pictureName)
    os.remove(picture_path)
    

def fillForm(form, studentData):
    form.registrationNumber.data = studentData.registrationNumber
    form.picture.data = studentData.picture
    form.frenchLastName.data = studentData.frenchLastName
    form.frenchFirstName.data = studentData.frenchFirstName
    form.arabicLastName.data = studentData.arabicLastName
    form.arabicFirstName.data = studentData.arabicFirstName
    form.grade.data = studentData.grade
    form.nationality.data = studentData.nationality
    form.bloodGroup.data = studentData.bloodGroup
    form.birthDate.data = studentData.birthDate
    form.birthPlace.data = studentData.birthPlace
    form.fatherName.data = studentData.fatherName
    form.fatherProfession.data = studentData.fatherProfession
    form.motherName.data = studentData.motherName
    form.motherProfession.data = studentData.motherProfession
    form.address.data = studentData.address
    form.parentsDivorced.data = studentData.parentsDivorced
    form.fatherDead.data = studentData.fatherDead
    form.fatherDeathDate.data = studentData.fatherDeathDate
    form.motherDead.data = studentData.motherDead
    form.motherDeathDate.data = studentData.motherDeathDate
    form.siblingsNumber.data = studentData.siblingsNumber
    form.joiningDate.data = studentData.joiningDate
    form.arrivalDate.data = studentData.arrivalDate
    form.departureDate.data = studentData.departureDate
    form.phoneNumber.data = studentData.phoneNumber
    form.parentPhoneNumber.data = studentData.parentPhoneNumber

    return form
    
def reassignStudentInfo(student, form):
    student.registrationNumber = form.registrationNumber.data
    student.frenchLastName = form.frenchLastName.data
    student.frenchFirstName = form.frenchFirstName.data
    student.arabicLastName = form.arabicLastName.data
    student.arabicFirstName = form.arabicFirstName.data
    student.grade = form.grade.data
    student.nationality = form.nationality.data
    student.bloodGroup = form.bloodGroup.data
    student.birthDate = form.birthDate.data
    student.birthPlace = form.birthPlace.data
    student.fatherName = form.fatherName.data
    student.fatherProfession = form.fatherProfession.data
    student.motherName = form.motherName.data
    student.motherProfession = form.motherProfession.data
    student.address = form.address.data
    student.parentsDivorced = form.parentsDivorced.data
    student.fatherDead = form.fatherDead.data
    student.fatherDeathDate = form.fatherDeathDate.data
    student.motherDead = form.motherDead.data
    student.motherDeathDate = form.motherDeathDate.data
    student.siblingsNumber = form.siblingsNumber.data
    student.joiningDate = form.joiningDate.data
    student.arrivalDate = form.arrivalDate.data
    student.departureDate = form.departureDate.data
    student.phoneNumber = form.phoneNumber.data
    student.parentPhoneNumber = form.parentPhoneNumber.data
    return student


def createStudent(form):
    student = Student(
        registrationNumber = form.registrationNumber.data,
        picture = saveStudentPicture(form.picture.data, None),
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
    return student
    


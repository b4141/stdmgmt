from datetime import datetime
from stdmgmt import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registrationNumber = db.Column(db.String(100), unique=True, nullable=False)
    picture = db.Column(db.String(300), unique=True, nullable=False)
    frenchLastName = db.Column(db.String(100), nullable=False)
    frenchFirstName = db.Column(db.String(100), nullable=False)
    arabicLastName = db.Column(db.String(100), nullable=False)
    arabicFirstName = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(100), nullable=False)
    nationality = db.Column(db.String(100), nullable=False)
    bloodGroup = db.Column(db.String(100), nullable=False)

    birthDate = db.Column(db.Date, nullable=False)

    birthPlace = db.Column(db.String(100), nullable=False)
    fatherName = db.Column(db.String(100), nullable=False)
    fatherProfession = db.Column(db.String(100))
    motherName = db.Column(db.String(100), nullable=False)
    motherProfession = db.Column(db.String(100))
    address = db.Column(db.String(100), nullable=False)

    parentsDivorced = db.Column(db.Boolean, default=False)
    fatherDead = db.Column(db.Boolean, default=False)
    motherDead = db.Column(db.Boolean, default=False)
    fatherDeathDate = db.Column(db.Date)
    motherDeathDate = db.Column(db.Date)

    siblingsNumber = db.Column(db.Integer, nullable=False, default=0)
    joiningDate = db.Column(db.Date, nullable=False)
    arrivalDate = db.Column(db.Date)
    departureDate = db.Column(db.Date)
    phoneNumber = db.Column(db.String(100), nullable=False)
    parentPhoneNumber = db.Column(db.String(100))

    def __repr__(self):
        return f"sn: {self.registrationNumber}, lastName: {self.frenchLastName}, jDate: {self.joiningDate}"


    def fullDict(self):
        return {
            'registrationNumber': self.registrationNumber,
            'picture': self.picture,
            'frenchLastName': self.frenchLastName,
            'frenchFirstName': self.frenchFirstName,
            'arabicLastName': self.arabicLastName,
            'arabicFirstName': self.arabicFirstName,
            'grade': self.grade,
            'nationality': self.nationality,
            'bloodGroup': self.bloodGroup,
            'birthDate': self.birthDate,
            'birthPlace': self.birthPlace,
            'fatherName': self.fatherName,
            'fatherProfession': self.fatherProfession,
            'motherName': self.motherName,
            'motherProfession': self.motherProfession,
            'address': self.address,
            'parentsDivorced': self.parentsDivorced,
            'fatherDead': self.fatherDead,
            'motherDead': self.motherDead,
            'fatherDeathDate': self.fatherDeathDate,
            'motherDeathDate': self.motherDeathDate,
            'siblingsNumber': self.siblingsNumber,
            'joiningDate': self.joiningDate,
            'arrivalDate': self.arrivalDate,
            'departureDate': self.departureDate,
            'phoneNumber': self.phoneNumber,
            'parentPhoneNumber': self.parentPhoneNumber,
            'submit': False,
            'csrf_token': None,
        }
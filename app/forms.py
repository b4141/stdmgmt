from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DateField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length, NumberRange

class StudentRegistrationForm(FlaskForm):
    registrationNumber = StringField('registrationNumber', validators=[DataRequired(), Length(min=2, max=100)])
    frenchLastName = StringField('frenchLastName', validators=[DataRequired(), Length(min=2, max=100)])
    frenchFirstName = StringField('frenchFirstName', validators=[DataRequired(), Length(min=2, max=100)])
    arabicLastName = StringField('arabicLastName', validators=[DataRequired(), Length(min=2, max=100)])
    arabicFirstName = StringField('arabicFirstName', validators=[DataRequired(), Length(min=2, max=100)])
    grade = StringField('grade', validators=[DataRequired(), Length(min=2, max=100)])
    nationality = StringField('nationality', validators=[DataRequired(), Length(min=2, max=100)])
    bloodGroup = SelectField('bloodGroup', choices=[('O-', 'O-'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O+', 'O+'), ('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+')], validators=[DataRequired()])
    birthDate = DateField('birthDate', validators=[DataRequired()])
    birthPlace = StringField('birthPlace', validators=[DataRequired(), Length(min=2, max=100)])

    fatherName = StringField('fatherName', validators=[DataRequired(), Length(min=2, max=100)])
    fatherProfession = StringField('fatherProfession', validators=[DataRequired(), Length(min=2, max=100)])
    motherName = StringField('motherName', validators=[DataRequired(), Length(min=2, max=100)])
    motherProfession = StringField('motherProfession', validators=[DataRequired(), Length(min=2, max=100)])
    address = StringField('address ', validators=[DataRequired(), Length(min=2, max=100)])

    parentsDivorced = BooleanField('parentsDivorced')
    fatherDead = BooleanField('fatherDead')
    fatherDeathDate = DateField('fatherDeathDate')
    motherDead = BooleanField('motherDead')
    motherDeathDate = DateField('motherDeathDate')

    siblingsNumber= IntegerField('siblingsNumber ', validators=[DataRequired()])
    joiningDate = DateField('joiningDate', validators=[DataRequired()])
    arrivalDate = DateField('arrivalDate', validators=[DataRequired()])
    departureDate = DateField('departureDate', validators=[DataRequired()])
    phoneNumber = StringField('phoneNumber', validators=[DataRequired(), Length(min=2, max=100)])
    parentPhoneNumber = StringField('parentPhoneNumber', validators=[Length(min=2, max=100)])
    submit = SubmitField('Submit')


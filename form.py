from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField, ValidationError, validators
from wtforms.validators import DataRequired, Email, Regexp
import requests
import phonenumbers
import re

###### form.py
#   Coding challenge for Lightfeather
#   @author Joseph Ashley <joseph.ashley@protonmail.com>
#   @date   2021-09-16
######

API_URL = 'http://127.0.0.1:8080'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'oo3AS0Ko8HPedhcD4MICvocaH2ntii2ZMT568zqq6k7u2bobcU8Auzrx18BG'
Bootstrap(app)

### Web Form Construct
class TestForm(FlaskForm):
    supervisor_choices = requests.get(API_URL+'/api/supervisors')
    supervisor_choices = supervisor_choices.json()

    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    contactMethod = SelectField('Preferred Contact Method', choices={"Email", "Phone"}, validators=[DataRequired()])
    phone = StringField('Phone Number')
    email = StringField('Email Address') #, validators=[Email()])
    supervisor = SelectField('Supervisor', choices=supervisor_choices, validators=[DataRequired()])
    submit = SubmitField('Submit')

### Main application
@app.route("/", methods=['GET', 'POST'])
def index():
    ## Create form    
    form = TestForm()
    
    if form.validate_on_submit():

        ## Pull data from form
        firstName = form.firstName.data
        lastName = form.lastName.data
        contactMethod = form.contactMethod.data
        phone = form.phone.data
        email = form.email.data
        supervisor = form.supervisor.data
        number = ""

        ## Validations
        is_valid = True # Initial condition

        # Names
        if not (firstName.isalpha() and lastName.isalpha()):
            is_valid = False
            print("\n    Names must be alphabetic only. \n")

        # Phone number
        if phone == '' or phone == None:
            if contactMethod == "Phone":
                is_valid == False
                print("\n    Please enter a valid phone number. \n")
        else:
            z = phonenumbers.parse(phone,"US")
            if phonenumbers.is_valid_number(z):
                number = phonenumbers.format_number(z, phonenumbers.PhoneNumberFormat.NATIONAL)
            else:
                is_valid = False
                print("\n    Please enter a valid phone number. \n")

        # Email
        if email == '' or email == None:
            if contactMethod == "Email":
                is_valid = False
                print("\n    Please enter a valid email. \n")
        else:
            if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
                is_valid = False
                print("\n    Please enter a valid email. \n")

        
        ## Submit if successful
        if is_valid:
            info = {
                'firstName': firstName,
                'lastName': lastName,
                'email': email,
                'phone': number,
                'supervisor': supervisor,
                'contactMethod': contactMethod
                }
            requests.post(API_URL+'/api/submit', json = info)
            print("\n    Notification subscription complete. \n")
        
    ## Otherwise...
    message = "Submission failed"
    supervisors = requests.get(API_URL+'/api/supervisors')
    return render_template('index.html', supervisors=supervisors, form=form, message=message)

## Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Start the main thread
if __name__ == '__main__':
    app.run( port=5000)

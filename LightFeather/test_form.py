from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField, ValidationError #, validators
from wtforms.validators import DataRequired, Email, Regexp
import requests
import re

API_URL = 'http://127.0.0.1:8080'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'oo3AS0Ko8HPedhcD4MICvocaH2ntii2ZMT568zqq6k7u2bobcU8Auzrx18BG'
Bootstrap(app)


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


@app.route("/", methods=['GET', 'POST'])
def index():
    supervisors = requests.get(API_URL+'/api/supervisors')    
    form = TestForm()
    if form.validate_on_submit():
        firstName = form.firstName.data
        lastName = form.lastName.data
        contactMethod = form.contactMethod.data
        phone = form.phone.data
        email = form.email.data
        supervisor = form.supervisor.data
        info = {
            'firstName': firstName,
            'lastName': lastName,
            'email': email,
            'phone': phone,
            'supervisor': supervisor
            }
        if contactMethod == "Email":
            if not (email == None or email == '') and re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
                requests.post(API_URL+'/api/submit', json = info)
                #flash("Your submission is successful")
            else:
                print("Please enter a valid email.")
            #    raise ValidationError(f"Please enter a valid email.")
        else:
            number = str(re.findall(r'\d+', phone))
            print(number[0])
            #if (len(number)>=7 and len(number)<=11):
            if not (phone == None or phone == ''):
                requests.post(API_URL+'/api/submit', json = info)
                #flash("Your submission is successful")
            else:
                print("Please enter a valid phone number.")
            #    raise ValidationError(f"Please enter a valid phone number.")
        #requests.post(API_URL+'/api/submit', json = info)
        #message = "Submission successful"
        
    
    message = "Submission failed"
    return render_template('index.html', supervisors=supervisors, form=form, message=message)




@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run( port=5000)
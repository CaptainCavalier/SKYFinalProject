from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm


# inheritancedef user_check(user_name):
# BasicForm inherits from FlaskForm
# BasicForm is now a kind of FlaskForm
class BasicForm(FlaskForm):
    # instantiating various input fields
    user_name = StringField('Username')
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    age = StringField('Age')
    email = StringField('Email Address')
    submit = SubmitField('Create Membership')


class VehicleForm(FlaskForm):
    car_type = StringField('What type of car are you looking for?')
    submit = SubmitField('Find me a car')

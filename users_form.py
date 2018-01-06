from Flask import flask, render_template
from wtforms import Form, StringField, PasswordField, IntegerField, validators
from wtforms_validator import InputRequired, Email, Length, AnyOf

class UsersForm(Form):
	length_of_road = IntegerField('lenqth_of_road', validators=[validators.required(), validators.length(min=1, max=10)])
	price_for_road = IntegerField('price_for_road', validators=[validators.required(), validators.length(min=1, max=10)])
	price_tur = IntegerField('price_tur', validators=[validators.required()])

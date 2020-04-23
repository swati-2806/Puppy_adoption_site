from flask_wtf import FlaskForm
from wtforms import StringField,TextField,SubmitField,IntegerField

class AddForm(FlaskForm):
	name=StringField("Name of Puppy: ")
	submit=SubmitField('Add Puppy')


class Delform(FlaskForm):
	id=IntegerField('Enter Id of the puppy to be deleted: ')
	submit=SubmitField('Remove Puppy')


class AddOwner(FlaskForm):
	name=StringField('Enter name of the owner:')
	id=IntegerField('Enter id of the puppy:')
	submit=SubmitField('Add Owner')
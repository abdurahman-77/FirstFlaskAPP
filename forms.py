
from flask_wtf import FlaskForm  #type: ignore
from wtforms import StringField,SubmitField #type: ignore
from wtforms.validators import DataRequired #type: ignore

class AddTaskForm(FlaskForm):

  title=StringField("Title", validators =[DataRequired()] ) #type: ignore #to check whether the field is blank or not necessary
  submit = SubmitField("Submit")

class DeleteTaskForm(FlaskForm):
  submit = SubmitField("Delete")
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import  TextAreaField
from wtforms.validators import InputRequired

class UploadForm(FlaskForm):
    description = TextAreaField('Description',validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(["jpg","jpeg","png"], 'Images only!')])

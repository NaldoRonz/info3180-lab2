from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FileField, TextAreaField
from wtforms.validators import Required, Regexp, Length, Email
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import ValidationError
from flask_uploads import UploadSet, IMAGES

images = UploadSet("images", IMAGES)

class add_Profile(FlaskForm):
    Firstname = StringField("Firstname", validators = [Required(), Length(min=2, max=20), Regexp("[A-Z][a-z]*")])
    Lastname = StringField("Lastname", validators = [Required(),  Length(min=2, max=20), Regexp("[A-Z]+([ '-][a-zA-Z]+)*")])
    Gender = SelectField("Gender", choices = [("N/A","---"),("M","Male"),("F","Female"), ("O","Other")], validators = [Required()])
    Email = StringField("Email", validators = [Required(), Email()])
    Location = StringField("Location", validators = [Required()])
    Biography = TextAreaField("Biography", validators = [Required()])
    Browse = FileField("images", validators =[FileRequired(), FileAllowed(images, "Please only upload image files only!!!")])

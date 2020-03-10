from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FileField
from wtforms.validators import Required, Regexp, Length, Email
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import ValidationError
from flask_uploads import UploadSet, IMAGES

images = UploadSet("images", IMAGES)

class add_Profile(FlaskForm):
    Firstname = StringField("Firstname", validators = [Required(), Regexp('([A-Za-z0-9\. -]+)',0,'First name must only have letters and must be greater than 1 in length')])
    Lastname = StringField("Lastname", validators = [Required(), Regexp("([A-Za-z0-9\. -]+)")])
    Gender = SelectField("Gender", choices = [("N/A","---"),("M","Male"),("F","Female"), ("O","Other")], validators = [Required()])
    Email = StringField("Email", validators = [Required(), Email()])
    Location = StringField("Location", validators = [Required()])
    Browse = FileField("images", validators =[FileRequired(), FileAllowed(images, "Please only upload image files only!!!")])

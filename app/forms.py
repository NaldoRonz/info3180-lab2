from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email

class add_Profile(FlaskForm):
    Firstname = StringField("Firstname", validators = [DataRequired()])
    Lastname = StringField("Lastname", validators = [DataRequired()])
    Gender = StringField("Gender", validators = [DataRequired()])
    Email = StringField("Email", validators = [DataRequired(),Email()])
    Location = StringField("Location", validators = [DataRequired()])

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired,Length

class User(FlaskForm):
    password = StringField(validators=[DataRequired(),Length(min=8)])
    user_name = StringField(validators=[DataRequired(),Length(max=25)])
    
    class Meta:
        csrf = False
    

class AddUser(User):
    name = StringField(validators=[DataRequired(),Length(max=50)])
    


class ValidateUser(User):
    pass



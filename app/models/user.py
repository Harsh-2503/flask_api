import mongoengine as db


class User(db.Document):
    name = db.StringField(required=True,max_length=50)
    user_name = db.StringField(unique=True,required=True,max_length=25)
    password = db.StringField(required=True,min_length=8)
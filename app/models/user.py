import mongoengine as db
from datetime import datetime


class User(db.Document):
    created_at = db.DateTimeField(default=datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.utcnow)
    name = db.StringField(required=True,max_length=50)
    user_name = db.StringField(unique=True,required=True,max_length=25)
    password = db.StringField(required=True,min_length=8)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        return super(User, self).save(*args, **kwargs)
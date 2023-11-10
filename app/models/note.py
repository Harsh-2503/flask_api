import mongoengine as db
from app.models.user import User


class Note(db.Document):
    name = db.StringField()
    heading = db.StringField()
    description = db.StringField(required=True)
    user = db.ReferenceField(User,reverse_delete_rule=2)
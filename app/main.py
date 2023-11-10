from flask import Flask, render_template, request, redirect
from config import MONGO_URI,JWT_SECRET_KEY
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from app.services.custom_jwt_error_handlers import(

    custom_invalid_token_callback,
    custom_unauthorized_callback,
    custom_expired_token_callback,
)

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['MONGODB_SETTINGS'] = {
"host":MONGO_URI
}
jwt = JWTManager(app)

jwt.invalid_token_loader(custom_invalid_token_callback)
jwt.unauthorized_loader(custom_unauthorized_callback)
jwt.expired_token_loader(custom_expired_token_callback)


# app.config.from_object('config')
# mongo = PyMongo(app)

mongo = MongoEngine()
mongo.init_app(app)

from app.v1.main import bp as auth_bp
app.register_blueprint(auth_bp,url_prefix="/v1")




    

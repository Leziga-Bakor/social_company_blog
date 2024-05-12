import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY']='mysecret'

####################################
######### DATABSASE SETUP ##########
####################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

###########################
#### LOGIN CONFIGS ########
###########################

login_manager = LoginManager()

# We can now pass in our app to the login manager
login_manager.init_app(app)

# Tell users what view to go to when they need to login.
login_manager.login_view = "users.login"


###########################
#### Blueprints config ####
###########################

#Import of Bluebrints
from companyBlog.core.views import core
from companyBlog.error_pages.handlers import error_pages
from companyBlog.users.views import users

# Registration of blueprints
app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
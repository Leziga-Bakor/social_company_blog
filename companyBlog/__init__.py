import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

####################################
### DATABSASE SETUP ################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABSASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


from companyBlog.core.views import core
from companyBlog.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)
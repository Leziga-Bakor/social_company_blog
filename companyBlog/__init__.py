from flask import Flask

app = Flask(__name__)

from companyBlog.core.views import core
from companyBlog.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)
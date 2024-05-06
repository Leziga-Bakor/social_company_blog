from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from companyBlog import db
from companyBlog.models import User, BlogPost
from companyBlog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from companyBlog.users.picture_handler import add_profile_pic

users = Blueprint('users',__name__)
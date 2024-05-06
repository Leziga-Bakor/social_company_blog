from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from companyBlog import db
from companyBlog.models import User, BlogPost
from companyBlog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from companyBlog.users.picture_handler import add_profile_pic

users = Blueprint('users',__name__)

# register
@users.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email = form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thank you for registering')
        return redirect(url_for('user.login'))
    
    return render_template('register.html',form=form)

# login

# logout
@users.route("/logout")
def logout():
    login_user()
    return redirect(url_for("core.index"))

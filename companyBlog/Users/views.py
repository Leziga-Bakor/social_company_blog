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
@users.route('/login',method=['GET','POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Login Successful')

            next = request.args.get('next')
            if next == None or not next[0]=='/':
                return redirect(next)
            return redirect(next)
    return render_template('login.html', form=form)

# logout
@users.route("/logout")
def logout():
    login_user()
    return redirect(url_for("core.index"))

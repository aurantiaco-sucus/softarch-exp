from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user


from .forms import LoginForm, RegistrationForm
from . import auth
from ..models import User
from .. import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # 创建登录表单对象
    if form.validate_on_submit():
        # 查询数据库中的用户名和密码是否与输入的匹配
        user = User.query.filter_by(name=form.username.data,
                                    password=form.password.data).first()
        if user:
            login_user(user)
            return redirect(url_for('main.index'))

    return render_template('login.html',
                           title='登录',
                           form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()  # 创建注册表单对象
    if form.validate_on_submit():
        # 在数据库中用户表中添加对应的记录
        user = User(email=form.email.data,
                    name=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('注册成功')
        # 注册成功后跳转到登录页面
        return redirect(url_for('auth.login'))

    return render_template('register.html',
                           title='注册',
                           form=form)

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

from flask import Flask, render_template, request, flash



from .forms import LoginForm
from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # 创建登录表单对象
    return render_template('login.html',
                           title='登录',
                           form=form)

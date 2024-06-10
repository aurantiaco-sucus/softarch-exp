from flask import Flask, render_template
from flask_login import login_required

from . import main

@main.route('/')
def index():
    return render_template('index.html',
                           title='首页')



@main.route('/services')
@login_required
def services():
    return 'Services'



@main.route('/about')
def about():
    return 'About'



@main.route('/projects')
def projects():
    return 'Projects'

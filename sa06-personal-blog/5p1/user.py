from flask import Blueprint



user = Blueprint('user', __name__)



@user.route('/index')
def index():
    return 'user_index'



@user.route('/show')
def show():
    return 'user_show'



@user.route('/add')
def add():
    return 'user_add'

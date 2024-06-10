from flask import Blueprint



admin = Blueprint('admin', __name__)



@admin.route('/index')
def adminindex():
    return 'admin_index'



@admin.route('/show')
def adminshow():
    return 'admin_show'



@admin.route('/add')
def adminadd():
    return 'admin_add'


from flask import Flask, render_template, request
from markdown import markdown
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *


app = Flask(__name__)
bootstrap = Bootstrap(app)
nav = Nav()
navbar = Navbar('Bootstrap测试',
                View('主页', 'index'),
                View('服务', 'services'),
                View('项目', 'projects'),
                View('关于', 'about'))
nav.register_element('top', navbar)
nav.init_app(app)


@app.route('/')
def index():
    return render_template('index.html',
                           title = '首页')



@app.route('/services')
def services():
    return 'Services'



@app.route('/about')
def about():
    return 'About'



@app.route('/projects')
def projects():
    return 'Projects'

@app.template_test('current_link')
def is_current_link(link):
    return link == request.path



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

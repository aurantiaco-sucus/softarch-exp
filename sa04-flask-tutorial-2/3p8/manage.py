from flask import Flask, render_template, request, flash
from markdown import markdown
from flask_bootstrap import Bootstrap
from forms import LoginForm


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_pyfile('config')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm() # 创建登录表单对象
    flash('登录成功')
    return render_template('login.html',
                           title='登录',
                           form=form)





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

import os

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter

@app.route('/')
def hello_world():
    return render_template('index.html', title='congratulation')


@app.route('/services')
def services():
    return 'Services'


@app.route('/about')
def about():
    return 'about'


@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return 'result:%s' % (a+b)


@app.route('/user/<regex("[a-z]{3}"):username>')
def user(username):
    return 'user:%s' % username


@app.route('/services/') # 目录
def services_dir():
    return 'Services'


@app.route('/projects/')
@app.route('/myworks/')
def projects():
    return 'projects'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        username = request.args['username']
        print('get:username=%s' % username)
    else: # 'POST'
        username = request.form['username']
        password = request.form['password']
        print('post:username=%s,password=%s' % (username, password))
    return render_template('login.html',
                           method=request.method)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # 获取上传文件的信息
        f = request.files['file']
        # 获取当前文件所在的路径
        basepath = os.path.abspath(os.path.dirname(__file__))
        # 上传的文件一般需要放到 static 目录下
        uploadpath = os.path.join(basepath, 'static/uploads', f.filename)
        # 保存文件
        f.save(uploadpath)
        # 重新跳转到upload路由
        return redirect(url_for('upload'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

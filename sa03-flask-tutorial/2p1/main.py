from flask import Flask, render_template, request
from werkzeug.routing import BaseConverter

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter

@app.route('/user/<regex("[a-z]{3}"):username>')
def user(username):
    return 'user:%s' % username

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return 'result:%s' % (a+b)

@app.route('/services/') # 目录
def services():
    return 'Services'

@app.route('/about') # 文件
def about():
    return 'about'

@app.route('/projects/')
@app.route('/myworks/')
def projects():
    return 'projects'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
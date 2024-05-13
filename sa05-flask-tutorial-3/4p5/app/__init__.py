from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from flask_sqlalchemy import SQLAlchemy
from app.views import init_view

bootstrap = Bootstrap()
nav = Nav()
db = SQLAlchemy()

from app.models import *

# 创建 app 对象的函数
def create_app():
    # 1 创建 app 对象 然后进行配置
    app = Flask(__name__)
    # 引入 secret_key
    app.config.from_pyfile('config')
    # 配置数据库的连接 参数包括：登录用户名:登陆密码@主机名(端口号)/数据库名
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:2881/flasktest'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    init_view(app)

    # 2 把创建好的 app 对象给其他类或模块使用
    # 2.1 使用 app 对象作为参数对 bootstrap 对象进行初始化
    bootstrap.init_app(app)



    # 创建 Navbar 对象 作为导航栏显示的内容
    # 参数1 title 导航栏的标题
    # 其他参数 列表 显示导航条的各个项
    navbar = Navbar('Bootstrap测试',
                    View('主页', 'index'),
                    View('服务', 'services'),
                    View('项目', 'projects'),
                    View('关于', 'about'))
    nav.register_element('top', navbar)



    # 2.2 使用 app 对象作为参数对 nav 对象进行初始化
    nav.init_app(app)



    # 2.3 使用 app 对象作为参数对 db 对象进行初始化
    db.init_app(app)



    return app
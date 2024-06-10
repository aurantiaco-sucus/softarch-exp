from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_pagedown import PageDown
from flask_avatar import Avatar

bootstrap = Bootstrap()
nav = Nav()
db = SQLAlchemy()
pagedown = PageDown()
login_manager = LoginManager()
login_manager.login_view = 'auth.login' # 登录视图的名称
login_manager.login_message = '请先登录'
login_manager.login_message_category = 'info'

# 创建 app 对象的函数
# 创建 app 对象的函数
def create_app():
    # 1 创建 app 对象 然后进行配置
    app = Flask(__name__)
    # 引入 secret_key
    app.config.from_pyfile('config')
    # 配置数据库的连接 参数包括：登录用户名:登陆密码@主机名(端口号)/数据库名
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@127.0.0.1/flasktest'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    # 2 把创建好的 app 对象给其他类或模块使用
    # 2.1 使用 app 对象作为参数对 bootstrap 对象进行初始化
    bootstrap.init_app(app)

    # 创建 Navbar 对象 作为导航栏显示的内容
    # 参数1 title 导航栏的标题
    # 其他参数 列表 显示导航条的各个项
    navbar = Navbar('Bootstrap测试',
                    View('主页', 'main.index'),
                    View('服务', 'main.services'),
                    View('项目', 'main.projects'),
                    View('关于', 'main.about'))
    nav.register_element('top', navbar)

    # 2.2 使用 app 对象作为参数对 nav 对象进行初始化
    nav.init_app(app)

    # 2.3 使用 app 对象作为参数对 db 对象进行初始化
    db.init_app(app)

    # 2.4 使用 app 对象作为参数对视图进行初始化
    # init_view(app)

    login_manager.init_app(app)
    pagedown.init_app(app)
    Avatar(app)
    CSRFProtect(app)

    # 3 注册蓝图
    from .auth import auth
    from .main import main

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(main, static_folder='static')

    # 使用 app.template_test 装饰器把 python 中的函数装饰成模板函数
    # python 中的函数名 is_current_link 到了模板中就变成 current_link
    @app.template_test('current_link')
    def is_current_link(link):
        return link == request.path

    # 返回创建好的app
    return app

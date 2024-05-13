from flask import Flask, render_template, request, flash



from app.forms import LoginForm



def init_view(app):


    # 使用 app.template_test 装饰器把 python 中的函数装饰成模板函数
    # python 中的函数名 is_current_link 到了模板中就变成 current_link
    @app.template_test('current_link')
    def is_current_link(link):
        return link == request.path



    @app.route('/')
    def index():
        return render_template('index.html',
                               title='首页')



    @app.route('/services')
    def services():
        return 'Services'



    @app.route('/about')
    def about():
        return 'About'



    @app.route('/projects')
    def projects():
        return 'Projects'



    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()  # 创建登录表单对象
        return render_template('login.html',
                               title='登录',
                               form=form)


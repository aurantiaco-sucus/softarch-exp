# from flask_script import Manager
# from livereload import Server



from app import *



# 创建 app 对象
app = create_app()
# 创建Manager对象
# manager = Manager(app)



# @manager.command # 添加扩展命令
# def dev():
#     # 创建Server对象 并传递app
#     live_server = Server(app.wsgi_app)
#     # 指定监控的内容的目录
#     # 前面的**表示所有的目录
#     # 后面的*.*表示所有的文件
#     # 如果只是要监控 static 目录下的内容 可以写成 static/*.*
#     live_server.watch('**/*.*')
#     # 启动服务 指定open_url自动刷新
#     live_server.serve(open_url_delay=True)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # manager.run()

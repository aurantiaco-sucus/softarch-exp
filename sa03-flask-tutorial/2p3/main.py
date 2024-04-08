import os

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html',
                           title='congratulation')


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
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

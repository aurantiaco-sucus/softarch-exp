import os

from flask import Flask, render_template, make_response, request
from livereload import Server

app = Flask(__name__)


@app.route('/cookie')
def cookie():
    if request.cookies:
        try:
            print(request.cookies['username'])
        except:
            print('no data')
    template = render_template('index.html')
    response = make_response(template)
    response.set_cookie('username', 'lisi')
    return response


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')


if __name__ == '__main__':
    app.debug = True
    server = Server(app.wsgi_app)
    server.serve()

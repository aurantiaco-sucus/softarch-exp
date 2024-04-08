import os

from flask import Flask, render_template, make_response, request

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

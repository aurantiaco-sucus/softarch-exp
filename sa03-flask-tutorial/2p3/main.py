from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        username = request.args['username']
        print('get:username=%s' % username)
    else:  # 'POST'
        username = request.form['username']
        password = request.form['password']
        print('post:username=%s,password=%s' % (username, password))
    return render_template('login.html',
                           method=request.method)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

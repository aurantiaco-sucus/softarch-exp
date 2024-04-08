from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html',
                           title='congratulation')

@app.route('/services')
def services():
    return 'Services'

@app.route('/about')
def about():
    return 'about'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
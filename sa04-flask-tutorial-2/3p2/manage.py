from flask import Flask, render_template, request
from markdown import markdown



app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/services')
def services():
    return 'Services'



@app.route('/about')
def about():
    return 'About'



@app.route('/projects')
def projects():
    return 'Projects'

@app.template_test('current_link')
def is_current_link(link):
    return link == request.path



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

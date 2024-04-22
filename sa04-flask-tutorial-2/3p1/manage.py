from flask import Flask, render_template
from markdown import markdown

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html',
                           title='<h1>HelloWorld</h1>',
                           body='## Header')


@app.template_filter('md') # md是过滤器名称
def markdown_to_html(txt):
    return markdown(txt)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

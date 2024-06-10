from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_pagedown.fields import PageDownField


# 定义发布博客的类
class PostForm(FlaskForm):
    # 定义表单中的各个项
    title = StringField(label='标题', validators=[DataRequired()])
    body = PageDownField(label='正文', validators=[DataRequired()])
    submit = SubmitField(label='发表') # 提交按钮
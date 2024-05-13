from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired



# 定义表单类
# 定义表单类
class LoginForm(FlaskForm):
    # 定义表单中的各个项
    username = StringField(label='用户名', validators=[DataRequired()]) # 文本框 必须输入
    password = PasswordField(label='密码', validators=[DataRequired()]) # 密码框 必须输入
    submit = SubmitField() # 提交按钮

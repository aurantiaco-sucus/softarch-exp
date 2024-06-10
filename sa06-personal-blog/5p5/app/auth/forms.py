from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo



# 定义表单类
# 定义表单类
class LoginForm(FlaskForm):
    # 定义表单中的各个项
    username = StringField(label='用户名', validators=[DataRequired()]) # 文本框 必须输入
    password = PasswordField(label='密码', validators=[DataRequired()]) # 密码框 必须输入
    submit = SubmitField() # 提交按钮


class RegistrationForm(FlaskForm):
    # 定义表单中的各个项
    email = StringField(label='邮箱地址', validators=[DataRequired(),
                                                     Length(4, 32),
                                                     Email()])
    username = StringField(label='用户名', validators=[DataRequired(),
                                                       Length(4, 32),
                                                       Regexp('^[A-Za-z_][A-Za-z0-9_]*$', 0, '用户名必须由字母、数字、下划线组成，并以字母或下划线开头')])
    password = PasswordField(label='密码', validators=[DataRequired(),
                                                       EqualTo('password2')])
    password2 = PasswordField(label='确认密码', validators=[DataRequired()])
    submit = SubmitField('马上注册')
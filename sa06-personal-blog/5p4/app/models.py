from . import db, login_manager
from flask_login import UserMixin
from datetime import datetime


class Post(db.Model):
    # 表名
    __tablename__ = 'posts'
    # 表的字段
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=True)
    body = db.Column(db.String(200), nullable=True)
    body_html = db.Column(db.String(200), nullable=True)
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # 文章与用户的关系（多个文章对应一个用户）
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))


# 角色表
class Role(db.Model):
    # 表名
    __tablename__ = 'roles'
    # 表中的结构
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=True)
    # 角色与用户的关系（一个角色对应多个用户）
    # 通过backref进行反向作用 注意users并没有出现在数据库的字段中 这里只是Role类的一个引用而已
    users = db.relationship('User', backref='role')



# 用户表
class User(db.Model, UserMixin):
    # 表名
    __tablename__ = 'users'
    # 表中的结构
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(40), nullable=True)
    email = db.Column(db.String(20), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    # 用户与角色的关系（多个用户对应一个角色）
    # 通过ForeignKey指定外键
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    posts = db.relationship('Post', backref='author')

    @staticmethod
    def on_created(target, value, oldvalue, initiator):
        print('target:%s' % target)
        print('on_created:%s' % value)
        target.role = Role.query.filter_by(name='user').first()
        db.session.add(target)
        db.session.commit()


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


db.event.listen(User.name, 'set', User.on_created)

from flask import Flask, render_template, redirect, url_for
from flask_login import login_required, current_user



from . import main
from .forms import PostForm, CommentForm
from ..models import Post, Comment
from .. import db

@main.route('/')
def index():
    return render_template('index.html',
                           title='首页')

@main.route('/edit', methods=['GET', 'POST'])
@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id=0):
    if id == 0:
        post = Post(author_id=current_user.id)
    else:
        post = Post.query.get_or_404(id)



    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.post', id=post.id))



    title = '发布新博客'
    if id > 0:
        title = '编辑 - %s' % post.title


        form.title.data = post.title
        form.body.data = post.body



    return render_template('posts/edit.html',
                           title=title,
                           form=form)

@main.route('/services')
@login_required
def services():
    return 'Services'


@main.route('/about')
def about():
    return 'About'


@main.route('/projects')
def projects():
    return 'Projects'


@main.route('/post/<int:id>', methods=['GET', 'POST'])
@login_required
def post(id): # 评论的 id 必须大于0
    post = Post.query.get_or_404(id)



    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(body=form.body.data,
                          post=post,
                          author=current_user)
        db.session.add(post)
        db.session.commit()


    return render_template('posts/detail.html',
                           title=post.title,
                           form=form,
                           post=post)
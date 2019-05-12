from app import app, db
from flask import render_template, flash, redirect, url_for, request
from .forms import LoginForm, RegistrationForm, PostForm
from flask_login import current_user, login_user, logout_user, login_required
from .models import User, Post


@app.route('/admin')
@login_required
def admin():
    posts = Post.query.all()
    return render_template('admin.html', posts=posts)


@app.route('/')
def home():
    q = request.args.get('q')
    if q:
        posts = Post.query.filter(Post.title.contains(q) |
                                  Post.title.contains(q.capitalize()) |
                                  Post.content.contains(q) |
                                  Post.content.contains(q.capitalize())
                                  )
    else:
        posts = Post.query.all()
    return render_template('home.html', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home'))
    return render_template('login_form.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('registration_form.html', title='Register', form=form)


@app.route('/users/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)
    return render_template('profile.html', user=user, posts=posts)


@app.route('/add_post', methods=['GET', 'POST'])
@login_required
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            author=current_user,
        )
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('home'))
    return render_template('add_post_form.html', form=form)


@app.route('/post/<post_id>/edit_post', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if current_user != post.author:
        flash('You can not edit this post')
        return redirect(url_for('post_detail', post_id=post_id))
    if request.method == "POST":
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post)
        if form.validate_on_submit():
            db.session.commit()
            flash('Your post is now edit!')
        return redirect(url_for('post_detail', post_id=post_id))
    form = PostForm(obj=post)
    return render_template('edit_post.html', post=post, form=form)


@app.route('/post/<post_id>/del', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if request.method == 'POST':
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted')
        return redirect(url_for('home'))
    return render_template('post_delete.html')


@app.route('/post/<post_id>', methods=['GET', 'POST'])
@login_required
def post_detail(post_id):
    post = Post.query.get(post_id)
    return render_template('post_detail.html', post=post)

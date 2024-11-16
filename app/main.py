import binascii
import os
from flask import Flask, render_template, redirect, flash, url_for, request
from flask_blog.app.db_connect import get_all_posts, get_post_id, write_data, update_data, delete_data
from forms.post import PostForm

app = Flask(__name__)

app.config['SECRET_KEY'] = binascii.hexlify(os.urandom(24))

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/posts', methods=['GET'])
def all_posts():
    posts = []
    get_posts = get_all_posts()
    for i in range(len(get_posts)):
        posts.append({'id': get_posts[i][0], 'title': get_posts[i][1], 'body': get_posts[i][2]})
    return render_template('post/posts.html', posts=posts)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    post_detail = get_post_id(post_id)
    post = {
        'title': post_detail[0][1],
        'body': post_detail[0][2]
    }
    return render_template('post/post.html', post=post)


@app.route('/create', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if request.method == 'POST':
        write_data(request.form.get('title'), request.form.get('body'))
        return redirect('posts')
    return render_template('post/post_create.html', form=form)


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update_post(post_id):
    post = get_post_id(post_id)
    if len(post) == 0:
        return redirect(url_for('all_posts'))

    form = PostForm(title=post[0][1], body=post[0][2])
    if form.validate_on_submit():
        update_data(post_id, form.title.data, form.body.data)
        return redirect(url_for('all_posts'))

    return render_template('post/post_update.html', form=form)


@app.route('/delete/<int:post_id>', methods=['GET'])
def delete_post(post_id):
    delete_data(post_id)
    return redirect(url_for('all_posts'))


if __name__ == '__main__':
    app.run(debug=True)

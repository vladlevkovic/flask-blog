import sqlite3

def connect_db():
    connect = sqlite3.connect('flaskblog.sqlite3')
    cursor = connect.cursor()
    return connect, cursor

# cursor.execute('''CREATE TABLE posts (
#     id INTEGER PRIMARY KEY,
#     title TEXT NOT NULL,
#     body TEXT NOT NULL
# )''')

# cursor.execute('INSERT INTO posts (title, body) VALUES (?,?)', ('First post', 'body 1'))
# cursor.execute('INSERT INTO posts (title, body) VALUES (?,?)', ('post 2', 'body 2'))
# cursor.execute('INSERT INTO posts (title, body) VALUES (?,?)', ('Lorem ipsum', 'body content'))
# connect.commit()

def get_all_posts():
    _, cursor = connect_db()
    data = cursor.execute('SELECT * FROM posts').fetchall()
    return data

def get_post_id(post_id):
    _, cursor = connect_db()
    data = cursor.execute('SELECT * FROM posts WHERE id = (?)', (post_id,)).fetchall()
    return data

def write_data(title, body):
    _, cursor = connect_db()
    cursor.execute('INSERT INTO posts (title, body) VALUES (?, ?)', (title, body))

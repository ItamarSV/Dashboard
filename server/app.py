from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_cors import CORS
from server.flaskmysql import get_books, new_book, update_book, delete_book
import os
import server.mysqlconnection as sql
import uuid

# configuration
DEBUG = True

# instantiate the app

template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'BooksApp')
template_dir = os.path.join(template_dir, 'client')
staticf = os.path.join(template_dir, 'dist')

app = Flask(__name__, template_folder=template_dir, static_folder=staticf)

app.config.from_object(__name__)
app.config['MYSQL_DATABASE_USER'] = sql.USER
app.config['MYSQL_DATABASE_PASSWORD'] = sql.PASSWORD
app.config['MYSQL_DATABASE_DB'] = sql.DATABASE
app.config['MYSQL_DATABASE_HOST'] = sql.HOST
mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()

BOOKS = get_books(conn)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        new_book(conn, post_data)
        BOOKS.append({
            'uuid': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
        # print(BOOKS)
    return jsonify(response_object)


@app.route('/books/<book_uuid>', methods=['PUT', 'DELETE'])
def single_book(book_uuid):
    book_id = get_book_id(book_uuid)
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        update_book(conn, post_data, book_id)
        commit = remove_book(book_uuid)
        print(commit)
        BOOKS.append({
            'uuid': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        delete_book(conn, book_id)
        remove_book(book_uuid)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


# @app.route('/', defaults={'path': 'index.html'})
# # def root(path):
# #     return render_template('dist/index.html')
# #
# @app.route('/<path:path>')
# def static_file(path):
#     return app.send_static_file(path)


def remove_book(book_uuid):
    for book in BOOKS:
        if book['uuid'] == book_uuid:
            BOOKS.remove(book)
            return True
    return False


def get_book_id(book_uuid):
    for book in BOOKS:
        if book['uuid'] == book_uuid:
            return book['uuid']
    return None


if __name__ == '__main__':
    app.run(host='0.0.0.0')


# export PYTHONPATH=/Users/itamarsvisa/CodeBase/BooksApp:$PYTHONPATH 
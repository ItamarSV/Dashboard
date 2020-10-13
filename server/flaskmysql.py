from flask import Flask
import pandas as pd
import datetime as dt
import uuid
from flaskext.mysql import MySQL
from server import mysqlconnection as sql


db = Flask(__name__)
db.config.from_object(__name__)
db.config['MYSQL_DATABASE_USER'] = sql.USER
db.config['MYSQL_DATABASE_PASSWORD'] = sql.PASSWORD
db.config['MYSQL_DATABASE_DB'] = sql.DATABASE
db.config['MYSQL_DATABASE_HOST'] = sql.HOST
mysql = MySQL()
mysql.init_app(db)
connection = mysql.connect()


def get_books(conn):
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM sql7360670.books WHERE (deleted_at IS NULL)""")
    data = cursor.fetchall()
    desc = cursor.description
    print('Commit: ' + str(conn.commit()))
    col_names = []
    for names in desc:
        col_names.append(names[0])

    books = pd.DataFrame(data)
    if not col_names:
        print('No col_name')
    else:
        books.columns = col_names

    for index, row in books.iterrows():
        books.loc[index, 'uuid'] = uuid.uuid4().hex

    books = books.to_dict('records')
    return books


def new_book(conn, post_data=None):
    cursor = conn.cursor()
    read = 0
    if post_data.get('read'):
        read = 1

    cursor.execute(
        f"""INSERT INTO `sql7360670`.`books` 
                (`title`, `author`, `read`, `price`) 
                VALUES 
                ('{post_data.get('title')}', '{post_data.get('author')}', '{read}', '99.99')"""
    )
    commit = conn.commit()
    print(commit)
    return commit


def update_book(conn, post_data=None, book_id=''):
    if book_id is None:
        print("Error: Didn't got book_id")
        return None
    cursor = conn.cursor()
    read = 0
    if post_data.get('read'):
        read = 1

    cursor.execute(
        f"""UPDATE `sql7360670`.`books` 
            SET `title` = '{post_data.get('title')}',
                `author` = '{post_data.get('author')}',
                `read` = '{read}'
            WHERE (`id` = '{book_id}');"""
    )
    commit = conn.commit()
    print(commit)
    return commit


def delete_book(conn, book_id=''):
    if book_id is None:
        print("Error: Didn't got book_id")
        return None
    cursor = conn.cursor()
    cursor.execute(
        f"""UPDATE `sql7360670`.`books` 
            SET `deleted_at` = '{dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
            WHERE (`id` = '{book_id}');"""
    )
    commit = conn.commit()
    print(commit)
    return commit


def manual_operation():
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM sql7360670.books WHERE (deleted_at IS NULL)""")
    data = cursor.fetchall()
    desc = cursor.description
    print('Commit: ' + str(connection.commit()))
    col_names = []
    for names in desc:
        col_names.append(names[0])

    books = pd.DataFrame(data)
    if not col_names:
        print('No col_name')
    else:
        books.columns = col_names

    for index, row in books.iterrows():
        books.loc[index, 'uuid'] = uuid.uuid4().hex

    books = books.to_dict('records')
    print(books)


manual_operation()

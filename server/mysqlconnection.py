import mysql.connector
from flaskext.mysql import MySQL
import pandas as pd
import json
import uuid

HOST = "sql7.freemysqlhosting.net"
DATABASE = "sql7360670"
USER = "sql7360670"
PASSWORD = "ECbZKTPbrj"

db_connection = mysql.connector.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)


def mysqlquery(query):
    cursor = db_connection.cursor()
    # query = ("SELECT * FROM sql7360670.books ")
    cursor.execute(query)
    data = cursor.fetchall()
    db_connection.commit()
    db_connection.close()
    desc = cursor.description
    col_names = []
    for names in desc:
        col_names.append(names[0])

    data = pd.DataFrame(data)
    data.columns = col_names
    # data = data.to_dict('records')
    # json.dumps(data)
    return data


# bookquery = ("SELECT * FROM sql7360670.books ")
# BOOKS = mysqlquery(query=bookquery)
# print(BOOKS)
#
# BOOKS['uuid'] = ''
# # for book in BOOKS:
# #     BOOKS[book].iloc['uuid'] = uuid.uuid4().hex
#
# for index, row in BOOKS.iterrows():
#     BOOKS.loc[index, 'uuid'] = uuid.uuid4().hex
#
# print(BOOKS['uuid'])

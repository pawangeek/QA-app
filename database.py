# Used to connect database of our application

# Every request pushes a new application context, wiping the old one,
# So g can be used to set flags per-request without change to code.

# Scope of g is per request (thread) and it will not retain the value in subsequent request

from flask import g
# import sqlite3
import psycopg2
from psycopg2.extras import DictCursor

# For sqlite3 connection

# def connect_db():
#     sql = sqlite3.connect('C:/Users/HP/PycharmProjects/qa-app/questions.db')  # You can put whole route there
#
#     # Row provides both index-based and case-insensitive name-based access to columns with almost no memory overhead.
#     # Better than your own custom dictionary-based approach or even a db_row based solution.
#
#     sql.row_factory = sqlite3.Row  # Returning an object that can also access columns by name
#     return sql
#
#
# def get_db():
#
#    # 'Hasattr main task is to check if an object has the given named attribute and return true if present, else false.
#    # Parameters obj: object whose which attribute has to be checked, key: Attribute which needs to be checked.
#
#     if not hasattr(g, 'sqlite.db'):
#         g.sqlite_db = connect_db()
#     return g.sqlite_db

# For postgres connection


def connect_db():

    conn = psycopg2.connect('postgres://zbhxmsnpsfygka:57a6e92af1b84a0a92bede8a1cec0223c05d0d9b8d7537eb6a246c902a5d30a3@ec2-34-225-82-212.compute-1.amazonaws.com:5432/dbna33ecoib6ob', cursor_factory=DictCursor)
    conn.autocommit = True
    sql = conn.cursor()

    return conn, sql


def get_db():
    db = connect_db()

    if not hasattr(g, 'postgres_db_conn'):
        g.postgres_db_conn = db[0]

    if not hasattr(g, 'postgres_db_cur'):
        g.postgres_db_cur = db[1]

    return g.postgres_db_cur


def init_db():
    db = connect_db()

    db[1].execute(open('schema.sql', 'r').read())
    db[1].close()

    db[0].close()

def init_admin():
    db = connect_db()

    db[1].execute('update users set admin = True where name = %s', ('Happy',))
    db[1].close()

    db[0].close()

import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# create table
cursor.execute("""CREATE TABLE books
(title TEXT, author TEXT, publisher TEXT, pub_date TEXT, isbn TEXT)""")

# # SQL - язык структурированных запросов
# # база данных -
# # СУБД- система управления базами данных
# # NOsql:SQL
# # posgreSQL,mySQL, SQLite3-2
#
# import sqlite3
#
# # CRUD - create reed update delete
# db = sqlite3.connect('op36_3.db')
# cursor = db.cursor()
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS user (
# lastname TEXT,
# age INTEGER,
# view INTEGER,
# bitday DATE
# )''')
#
# # CREATE - INSERT INTO
# # cursor.execute('''INSERT INTO user VALUES ("beka",49,5,'2003-87-99')''')
#
# # UPDATE-UPDATE
# cursor.execute('''UPDATE user SET age=99 WHERE rowid!=2 ''')
#
#
#
# # REED-SELECT,fech
# cursor.execute('''SELECT rowid,* FROM user''')
# a=cursor.fetchall()
# for i in a:
#     print(i)
#
#
# db.commit()
# db.close()
import sqlite3
def create_user_table():
    db = sqlite3.connect('op36_3.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user (
        lastname TEXT,
        age INTEGER,
        view INTEGER,
        bitday DATE
    )''')
    db.commit()
    db.close()


def delete_even_rowid():
    create_user_table()
    db = sqlite3.connect('op36_3.db')
    cursor = db.cursor()

    cursor.execute('''INSERT INTO user (lastname, age, view, bitday) VALUES (?, ?, ?, ?)''',
                   ('Doe', 30, 1, '1994-10-01'))
    cursor.execute('''INSERT INTO user (lastname, age, view, bitday) VALUES (?, ?, ?, ?)''',
                   ('Smith', 25, 2, '1990-05-15'))
    cursor.execute('''INSERT INTO user (lastname, age, view, bitday) VALUES (?, ?, ?, ?)''',
                   ('Johnson', 40, 3, '1985-12-25'))

    cursor.execute('''DELETE FROM user WHERE rowid % 2 = 0''')

    db.commit()
    db.close()

if __name__ == "__main__":
    delete_even_rowid()
# Python code to demonstrate table creation and
# insertions with SQL

# importing module
import sqlite3

# connecting to the database
connection = sqlite3.connect("userInfo.db")

# cursor
crsr = connection.cursor()


def create_table():
    # SQL command to create a table in the database
    sql_command = """CREATE TABLE IF NOT EXISTS signIn ( 
    username TEXT, 
    password TEXT);"""

    # execute the statement
    crsr.execute(sql_command)


def check_user(username):
    sql_command = """SELECT count(*) FROM signIn WHERE username = ?"""
    crsr.execute(sql_command, (username,))
    found = crsr.fetchone()[0]
    if found:
        return 1
    else:
        return 0


def check_pass(password):
    sql_command = """SELECT count(*) FROM signIn WHERE password = ?"""
    crsr.execute(sql_command, (password,))
    match = crsr.fetchone()[0]
    if match:
        return 1
    else:
        return 0


def insert_user_info(username, password):
    # SQL command to insert the data in the table
    sql_command = """INSERT INTO signIn (username, password) VALUES (?, ?);"""
    crsr.execute(sql_command, (username, password))


def close_db():
    # close the connection
    connection.commit()
    connection.close()
    return 0

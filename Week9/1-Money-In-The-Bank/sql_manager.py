import sqlite3
from client import Client
import hashlib
from datetime import datetime, timedelta

conn = sqlite3.connect("bank.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


def create_clients_table():
    # delete_table = "DROP TABLE IF EXISTS clients"
    # cursor.execute(delete_table)

    create_query = """
    CREATE TABLE IF NOT EXISTS clients
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
     username TEXT,
     password TEXT,
     balance REAL DEFAULT 0,
     message TEXT,
     num_login_tries INTEGER DEFAULT 0,
     last_login_try TEXT
     )
    """

    cursor.execute(create_query)
    # file_sql = "create_tables.sql"
    # with open(file_sql, "r") as f:
    #    pass
    #    conn.executescript(f.read())
    #   conn.commit()


def hash_password(password):
    byte_pass = str.encode(password)
    return hashlib.sha1(byte_pass).hexdigest()


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?"
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    new_pass = hash_password(new_pass)
    update_sql = "UPDATE clients SET password = ? WHERE id = ?"
    cursor.execute(update_sql, (new_pass, logged_user.get_id()))
    conn.commit()


def register(username, password):
    password = hash_password(password)
    print(password)
    insert_sql = "INSERT INTO clients (username, password) values (?, ?)"
    cursor.execute(insert_sql, (username, password))
    conn.commit()


def change_last_log_try(username):

    update_sql = "UPDATE clients SET last_login_try = ? , num_login_tries = num_login_tries + 1  WHERE username = ?"
    # + timedelta(days=1)
    now = datetime.now()

    cursor.execute(update_sql, (now, username))
    conn.commit()


def clear_brute_force(username):
    update_sql = "UPDATE clients SET num_login_tries = 0  WHERE username = ?"
    cursor.execute(update_sql, (username,))
    conn.commit()


def login(username, password):

    select_query = "SELECT id, username, password, balance, message, num_login_tries, last_login_try FROM clients WHERE username = ? LIMIT 1"

    cursor.execute(select_query, (username,))
    user = cursor.fetchone()

    if user is None:
        return {'err_index': 3, 'err_mess': 'Login failed'}
    else:
        string_date = user['last_login_try']
        last_log_try = datetime.strptime(string_date, "%Y-%m-%d %H:%M:%S.%f")
        last_try_log_date = user['num_login_tries']

        if last_log_try + timedelta(minutes=2) < datetime.now():
            clear_brute_force(username)
            last_try_log_date = 0

        if last_try_log_date > 4:
            return {'err_index': 1, 'err_mess': 'Bruteforce protection. Try again after 5min.'}
        elif user['password'] == hash_password(password):
            clear_brute_force(username)
            return Client(user[0], user[1], user[2], user[3])
        else:
            return {'err_index': 0, 'err_mess': 'Login failed'}

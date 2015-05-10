import sqlite3

db = sqlite3.connect('domains.db')
connect = db.cursor()


create_table_query = "CREATE TABLE IF NOT EXISTS domains(id INTEGER PRIMARY KEY, name VARCHAR(255),server VARCHAR(255),start_href VARCHAR(255))"
connect.execute(create_table_query)

create_table_query = "CREATE TABLE IF NOT EXISTS startbg_visited_domains(id INTEGER PRIMARY KEY, name VARCHAR(255))"
connect.execute(create_table_query)

create_index_query = "CREATE UNIQUE INDEX NameIndex On domains (name)"
create_index_query = "CREATE UNIQUE INDEX StartbgIndex On startbg_visited_domains(name)"
connect.execute(create_index_query)

db.commit()
db.close()

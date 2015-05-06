import sqlite3

db = sqlite3.connect('company.db')
connect = db.cursor()


create_table_query = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT,monthly_salary INTEGER,yearly_bonus INTEGER,position TEXT)"
result = connect.execute(create_table_query)
# result = connect.execute("DELETE FROM users")
insert_query = """
                INSERT INTO users
                VALUES
                    (1,'Ivan Ivanov',5000,10000,'Software Developer'),
                    (2,'Rado Rado',500,0,'Technical Support Intern'),
                    (3,'Ivo Ivo',10000,100000,'CEO'),
                    (4,'Petar Petrov',3000,1000,'Marketing Manager'),
                    (5,'Maria Georgieva',8000,10000,'COO')

"""

result = connect.execute(insert_query)

db.commit()
db.close()

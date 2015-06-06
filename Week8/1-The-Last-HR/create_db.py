import sqlite3

db = sqlite3.connect('hr.db')
connect = db.cursor()


create_table_courses_query = """
CREATE TABLE IF NOT EXISTS courses(
    course_id INTEGER PRIMARY KEY,
    name TEXT
)"""
connect.execute(create_table_courses_query)

create_table_students_query = """
CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    github TEXT
)"""
connect.execute(create_table_students_query)

create_table_students_query = """
CREATE TABLE IF NOT EXISTS students_to_courses(
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(student_id),
    FOREIGN KEY(course_id) REFERENCES students(course_id)
)"""
connect.execute(create_table_students_query)

db.commit()
db.close()
import requests
import sqlite3
db = sqlite3.connect('hr.db')
cursor = db.cursor()

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
req = requests.get('https://hackbulgaria.com/api/students/', headers=headers, allow_redirects=True)
students = req.json()


def empty_table(table_name):
        cursor.execute("DELETE FROM {}".format(table_name))
        db.commit()


def save_student(name, github):
    insert_student_query = """
    INSERT INTO students(name,github)
    VALUES(?,?)
    """
    cursor.execute(insert_student_query, (name, github))
    db.commit()
    return cursor.lastrowid


def save_course(name):
    insert_student_query = """
    INSERT INTO courses(name)
    VALUES(?)
    """
    cursor.execute(insert_student_query, (name,))
    db.commit()
    return cursor.lastrowid


courses_name_to_id = {}

empty_table('students')
i = 0
for student in students:
    student_id = save_student(student['name'], student['github'])
    for course in student['courses']:
        if course in courses_name_to_id:
            pass

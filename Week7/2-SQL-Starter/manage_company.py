import sqlite3

db = sqlite3.connect('company.db')
db.row_factory = sqlite3.Row
cursor = db.cursor()


def list_employees():
    result = cursor.execute("SELECT id,name,position FROM users")

    for row in result:
        print("{} - {} - {}".format(row[0], row[1], row[2]))


def mon_spend():
    result = cursor.execute("SELECT SUM(monthly_salary) FROM users")
    for row in result:
        return row[0]


def yearly_bonus():
    result = cursor.execute("SELECT SUM(yearly_bonus) FROM users")
    for row in result:
        return row[0]


def monthly_spending():
    spending = mon_spend()
    print("The company is spending ${} every month!".format(spending))


def yearly_spending():
    spending = mon_spend()*12 + yearly_bonus()
    print("The company is spending ${} every year!".format(spending))


def add_employee():
    name = input("name>")
    monthly_salary = input("monthly_salary>")
    yearly_bonus = input("yearly_bonus>")
    position = input("position>")

    query = "INSERT INTO users(name,monthly_salary,yearly_bonus,position) VALUES ('{}',{},{},'{}')".format(name,monthly_salary,yearly_bonus,position)
    cursor.execute(query)
    db.commit()


def delete_employee(em_id):

    query_name = "SELECT name FROM users WHERE id = {}".format(em_id)
    res = cursor.execute(query_name)
    row = res.fetchone()
    name = row['name']

    query = "DELETE FROM users WHERE id = {}".format(em_id)
    cursor.execute(query)
    db.commit()

    print("{} was deleted".format(name))


def update_employee(em_id):

    name = input("name>")
    monthly_salary = input("monthly_salary>")
    yearly_bonus = input("yearly_bonus>")
    position = input("position>")

    query = """
        UPDATE users SET name=?,monthly_salary=?,yearly_bonus=?,position=?
        WHERE id = ?
    """
    cursor.execute(query, (name, monthly_salary, yearly_bonus, position, em_id))
    db.commit()


commands = {
       "list_employees": list_employees,
       "monthly_spending": monthly_spending,
       "yearly_spending": yearly_spending,
       "add_employee": add_employee,
       "delete_employee": delete_employee,
       "update_employee": update_employee
}


def main():
    command = input("command> :")
    us_command = command.split()[0]
    try:
        em_id = command.split()[1]
        commands[us_command](em_id)
    except:
        commands[us_command]()


if __name__ == '__main__':
    main()

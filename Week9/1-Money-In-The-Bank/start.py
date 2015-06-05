import sql_manager
from logged_user import LoggedUser
from validate_registration import ValidateRegistration
from send_email import SendEmail
import string
import random
import getpass
from client import Client


def password_generator():
    size = 10
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(1, size))


def register():
    username = input("Enter your username: ")
    password = getpass.getpass('Enter your password:')

    valid_password = ValidateRegistration(username, password)
    is_valid = valid_password.is_valid()

    if is_valid is True:
        sql_manager.register(username, password)
        print("Registration Successfull")
    else:
        print(is_valid)


def login():
    username = input("Enter your username: ")
    password = getpass.getpass('Enter your password:')

    logged_user = sql_manager.login(username, password)

    if isinstance(logged_user, Client):
        user = LoggedUser(logged_user)
        user.user_menu()
    else:
        if logged_user['err_index'] == 0:
            sql_manager.change_last_log_try(username)
        else:
            pass
        print(logged_user['err_mess'])


def reset_password():
    username = input("(Reset Password)Enter your username: ")

    email_to = 'ivannborisov@gmail.com'
    email_text = "Your new password is :" + password_generator()
    email_subject = "Reset password"
    SendEmail.send_email(email_to, email_text, email_subject)


def help_menu():
    print("login - for logging in!")
    print("register - for creating new account!")
    print("exit - for closing program!")


def main_menu():
    print("Welcome to our bank service. You are not logged in.")
    print("Please register or login")

    commands = {
        'login': login,
        'help': help_menu,
        'register': register,
        'reset_password': reset_password

    }
    while True:
        command = input("$$$>")
        if command == 'exit':
            break
        # try:
        commands[command]()
        # except:
        # print("Not a valid command")


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()

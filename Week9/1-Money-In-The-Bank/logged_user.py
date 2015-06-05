import sql_manager


class LoggedUser():
    def __init__(self, user):
        self.__user = user

    def info(self):
        print("You are: " + self.__user.get_username())
        print("Your id is: " + str(self.__user.get_id()))
        print("Your balance is:" + str(self.__user.get_balance()) + '$')

    def changepass(self):
        new_pass = input("Enter your new password: ")
        sql_manager.change_pass(new_pass, self.__user)

    def change_message(self):
        new_message = input("Enter your new message: ")
        sql_manager.change_message(new_message, self.__user)

    def show_message(self):
        print(self.__user.get_message())

    def help_menu(self):
        print("info - for showing account info")
        print("changepass - for changing passowrd")
        print("change-message - for changing users message")
        print("show-message - for showing users message")

    def user_menu(self):

        commands = {
            'info': self.info,
            'changepass': self.changepass,
            'change-message': self.change_message,
            'show-message': self.show_message,
            'help': self.help_menu

        }
        print("Welcome you are logged in as: " + self.__user.get_username())
        while True:
            command = input("Logged>>")

            while True:
                command = input("$$$>")
                if command == 'exit':
                    break
                try:
                    commands[command]()
                except:
                    print("Not a valid command")

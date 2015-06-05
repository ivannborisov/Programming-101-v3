class ValidateRegistration:

    def __init__(self, username, password):
        self.__pass = password
        self.__username = username
        self.__errors = []

    def strong_pass(self):
        print (self.__username)
        if len(self.__pass) <= 8:
            self.__errors.append("Pass must be more than 8 symbols")
        if not any(x.isupper() for x in self.__pass):
            self.__errors.append('Your password needs at least 1 capital.')
        if not any(x.islower() for x in self.__pass):
            self.__errors.append('Your password needs at least 1 lower letter.')
        if self.__username in self.__pass:
            self.__errors.append('Username musnt be is not in the password (as a substring)')

    def is_valid(self):
        self.strong_pass()
        if len(self.__errors) == 0:
            return True
        else:
            return self.__errors

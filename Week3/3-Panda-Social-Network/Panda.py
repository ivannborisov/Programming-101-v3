import re


class Panda:

    def __init__(self, name, email, gender):

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise(ValueError)
        self.__name = str(name)
        self.__email = str(email)
        self.__gender = str(gender)

    def name(self):
        return self.__name

    def email(self):
        return self.__email

    def gender(self):
        return self.__gender

    def isMale(self):
        if self.__gender == 'male':
            return True
        else:
            return False

    def isFemale(self):
        if self.__gender == 'female':
            return True
        else:
            return False

    def __str__(self):
        return self.__name

    def __hash__(self):
        return hash(self.__name)

    def __repr__(self):
        return self.__name

    def __eq__(self, other):
        if self.__name == other.__name and self.__email == other.__email and self.__gender == other.__gender:
            return True
        else:
            return False

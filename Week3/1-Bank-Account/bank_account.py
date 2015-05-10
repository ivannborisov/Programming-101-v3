class BankAccount:

    def __init__(self, name, balance, currency):
        self.__balance = balance
        self.__name = name
        self.__currency = currency
        self.__history = ['Account was created']

    def deposit(self, val):
        self.__balance += val
        self.__history.append('Deposit {}{}'.format(val, self.__currency))

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def get_currency(self):
        return self.__currency

    def increase_bal(self, val):
        self.__balance += val

    def add_history(self, hist):
        self.__history.append(hist)

    def withdraw(self, val):
        if val > self.__balance:
            self.__history.append('Withdraw for {}{} failed'.format(val, self.__currency))
            return False
        self.__history.append("{}{} was withdrawed".format(val, self.__currency))
        self.__balance -= val
        return True

    def balance(self):
        self.__history.append('Balance check -> {}{}'.format(self.__balance, self.__currency))
        return self.__balance

    def transfer_to(self, other, val):
        if self.__currency != other.get_currency() or self.__balance < val:
            return False
        self.__balance -= val
        self.__history.append('Transfer to {} for {}{}'.format(other.get_name(), val, self.__currency))
        other.increase_bal(val)
        other.add_history('Transfer from {} for {}{}'.format(self.__name, val, self.__currency))
        return True

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.__name, self.__balance, self.__currency)

    def __int__(self):
        self.__history.append('__int__ check -> {}{}'.format(self.__balance, self.__currency))
        return self.__balance

    def history(self):
        return self.__history

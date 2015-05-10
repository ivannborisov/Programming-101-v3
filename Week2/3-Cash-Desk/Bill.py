class Bill:

    def __init__(self, amount):
        self.amount = amount

    def __int__(self):
        return self.amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(2*self.amount)

    def __eq__(self, other):
        return self.amount == other.amount

'''
a = Bill(10)
b = Bill(15)
c = Bill(10)
money_holder = {}

money_holder[a] = 1

if c in money_holder:
    money_holder[c] += 1

print(money_holder)
'''

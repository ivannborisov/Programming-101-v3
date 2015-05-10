from Bill import *
from BillBatch import *


class CashDesk:
    def __init__(self):
        self.money_list = []

    def take_money(self, money):

        if isinstance(money, Bill):
            self.money_list.append(money)

        if isinstance(money, BillBatch):
            batch_list = money.amlist
            for x in batch_list:
                self.money_list.append(x)

    def total(self):
        return sum(x.amount for x in self.money_list)

    def get_money_dict(self):
        money_dict = {}
        for x in self.money_list:
            if x in money_dict:
                money_dict[x] += 1
            else:
                money_dict[x] = 1
        return money_dict

    def inspect(self):
        m_dict = self.get_money_dict()
        print("We have a total of {}$ in the desk".format(self.total()))
        print("We have the following count of bills, sorted in ascending order:")
        for key in m_dict.keys():
            print('{}s - {}'.format(key, m_dict[key])[1:])



values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BillBatch(bills)

desk = CashDesk()


desk.take_money(batch)
desk.take_money(Bill(10))

desk.inspect()

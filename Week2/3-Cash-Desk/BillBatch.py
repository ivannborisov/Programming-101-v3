# import Bill
from Bill import *


class BillBatch:

    def __init__(self, amlist):
        self.amlist = amlist

    def __len__(self):
        return len(self.amlist)

    def total(self):
        return sum(x.amount for x in self.amlist)

    def __getitem__(self, index):
        return self.amlist[index]

    def getBatch():
        return self.amlist
'''
values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]

batch = BillBatch(bills)

print(batch.total())

for bill in batch:
    print(bill)
'''

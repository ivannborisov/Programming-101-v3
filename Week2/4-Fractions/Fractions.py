class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        if self.numerator % self.denominator == 0:
                    return str(self.numerator // self.denominator)
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if self.denominator == other.denominator:
            newNum = self.numerator + other.numerator
            return Fraction(newNum, self.denominator)
        else:
            newNum = self.numerator * other.denominator + other.numerator * self.numerator
            newDen = self.denominator * other.denominator
            return Fraction(newNum, newDen)

    def __sub__(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.numerator - other.numerator,self.denominator)
        else:
            newNum = self.numerator * other.denominator - other.numerator * self.numerator
            newDen = self.denominator * other.denominator
            return Fraction(newNum, newDen)

    def __eq__(self, other):
        first = self.numerator * other.denominator
        second = other.numerator * self.denominator

        if first == second:
            return True
        return False

    def __mul__(self, other):
        newNum = self.numerator * other.numerator
        newDen = self.denominator * other.denominator
        return Fraction(newNum, newDen)

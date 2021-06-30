import math


class Money:
    def __init__(self, five_hundred: int = 0,
                 one_hundred: int = 0,
                 fifty: int = 0,
                 twenty: int = 0,
                 ten: int = 0,
                 five: int = 0,
                 one: int = 0):
        self.five_hundred = five_hundred
        self.one_hundred = one_hundred
        self.fifty = fifty
        self.twenty = twenty
        self.ten = ten
        self.five = five
        self.one = one

    @property
    def total(self):
        return self.five_hundred * 500 + self.one_hundred * 100 + self.fifty * 50\
               + self.twenty * 20 + self.ten * 10 + self.five * 5 + self.one

    def __add__(self, other):
        if not isinstance(other, Money):
            raise TypeError(f'Type "Money" is expected, got {type(other)} instead!')
        other: Money

        self.five_hundred += other.five_hundred
        self.one_hundred += other.one_hundred
        self.fifty += other.fifty
        self.twenty += other.twenty
        self.ten += other.ten
        self.five += other.five
        self.one += other.one

    def __sub__(self, other):
        if not isinstance(other, Money):
            raise TypeError(f'Type "Money" is expected, got {type(other)} instead!')

        other: Money
        if self.total < other.total:
            raise ValueError('Balance becomes negative!')

        five_hundred, one_hundred, fifty, twenty, ten, five, one = 0,0,0,0,0,0,0
        diff = self.total - other.total
        if diff/500 > 1:
            five_hundred = math.floor(diff/500)
            diff -= five_hundred * 500
        if diff/100 > 1:
            one_hundred = math.floor(diff/100)
            diff -= one_hundred * 100
        if diff/50 > 1:
            fifty = math.floor(diff/50)
            diff -= fifty * 50
        if diff/20 > 1:
            twenty = math.floor(diff/20)
            diff -= twenty * 20
        if diff/10 > 1:
            ten = math.floor(diff/10)
            diff -= ten * 10
        if diff/5 > 1:
            five = math.floor(diff/5)
            diff -= five * 5
        if diff:
            one = diff

        self.five_hundred = five_hundred
        self.one_hundred = one_hundred
        self.fifty = fifty
        self.twenty = twenty
        self.ten = ten
        self.five = five
        self.one = one

    def __lt__(self, other):
        if not isinstance(other, Money):
            raise TypeError(f'Type "Money" is expected, got {type(other)} instead!')
        other: Money
        if self.total < other.total:
            return True
        else:
            return False

    def __gt__(self, other):
        if not isinstance(other, Money):
            raise TypeError(f'Type "Money" is expected, got {type(other)} instead!')
        other: Money
        if self.total > other.total:
            return True
        else:
            return False

    def __eq__(self, other):
        if not isinstance(other, Money):
            raise TypeError(f'Type "Money" is expected, got {type(other)} instead!')
        if self.total == other.total:
            return True
        else:
            return False

    def __str__(self):
        return f'Five_hundred: {self.five_hundred}, one_hundred: {self.one_hundred}, fifty: {self.fifty}, ' \
               f'twenty: {self.twenty}, ten: {self.ten}, five: {self.five}, one: {self.one}\n' \
               f'Total: {self.total}'

    def __repr__(self):
        return f'Money(five_hundred={self.five_hundred}, one_hundred={self.one_hundred}, fifty={self.fifty}, ' \
               f'twenty={self.twenty}, ten={self.ten}, five={self.five}, one={self.one})'
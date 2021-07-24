class Money:
    def __init__(self, banknotes):
        self.banknotes = banknotes

    @property
    def total(self):
        return sum([banknote*number
                    for banknote, number in self.banknotes.items()])

    def __add__(self, other):
        assert isinstance(other, Money), f'Type "Money" is expected,' \
                            f' got {type(other)} instead!'
        new_money = {}
        for banknote in banknotes_values:
            new_value = self.banknotes.get(banknote, 0) + other.banknotes.get(banknote, 0)
            if new_value:
                new_money[banknote] = new_value
        return Money(new_money)

    def __sub__(self, other):
        assert isinstance(other, Money), f'Type "Money" is expected,' \
                            f' got {type(other)} instead!'

        if self.total < other.total:
            raise ValueError('Balance becomes negative!')

        diff = self.total - other.total
        banknotes = divide_in_banknotes(diff)
        return Money(banknotes)

    def __lt__(self, other):
        if not isinstance(other, Money):
            raise TypeError(f'Type "Money" is expected,'
                            f' got {type(other)} instead!')
        return self.total < other.total

    def __gt__(self, other):
        if not isinstance(other, Money):
            raise TypeError(f'Type "Money" is expected,'
                            f' got {type(other)} instead!')
        return self.total > other.total

    def __eq__(self, other):
        if not isinstance(other, Money):
            raise TypeError(f'Type "Money" is expected,'
                            f' got {type(other)} instead!')
        return self.total == other.total

    def __str__(self):
        return f'{self.banknotes}, Total: {self.total}'

    def __repr__(self):
        return f'{self.banknotes}, Total:  {self.total}'


banknotes_values = 500, 100, 50, 20, 10, 5, 1


def divide_in_banknotes(total):
    banknotes = {}
    for value in banknotes_values:
        if total // value:
            banknotes[value], total = divmod(total, value)
    return banknotes

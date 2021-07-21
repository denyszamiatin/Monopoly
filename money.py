class Money:
    def __init__(self, banknotes):
        self.banknotes = banknotes

    @property
    def total(self):
        return sum([int(banknote)*self.banknotes[banknote]
                    for banknote in self.banknotes])

    def __add__(self, other):
        if not isinstance(other, Money):
            raise TypeError(f'Type "Money" is expected,'
                            f' got {type(other)} instead!')
        new_money = {}
        for i in self.banknotes:
            if i in other.banknotes.keys():
                new_money[i] = self.banknotes[i] + other.banknotes[i]
            else:
                new_money[i] = self.banknotes[i]
        for i in other.banknotes:
            if i not in self.banknotes.keys():
                new_money[i] = other.banknotes[i]
        return Money(new_money)

    def __sub__(self, other):
        if not isinstance(other, Money):
            raise TypeError(f'Type "Money" is expected,'
                            f' got {type(other)} instead!')

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


def divide_in_banknotes(total):
    banknotes = {}
    if total // 500:
        banknotes[500] = total // 500
        total %= 500
    if total // 100:
        banknotes[100] = total // 100
        total %= 100
    if total // 50:
        banknotes[50] = total // 50
        total %= 50
    if total // 20:
        banknotes[20] = total // 20
        total %= 20
    if total // 10:
        banknotes[10] = total // 10
        total %= 10
    if total // 5:
        banknotes[5] = total // 5
        total %= 5
    if total:
        banknotes[1] = total
    return banknotes
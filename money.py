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
            if not i in self.banknotes.keys():
                new_money[i] = other.banknotes[i]
        return Money(new_money)

    def __sub__(self, other):
        if not isinstance(other, Money):
            raise TypeError(f'Type "Money" is expected,'
                            f' got {type(other)} instead!')

        if self.total < other.total:
            raise ValueError('Balance becomes negative!')

        diff = self.total - other.total
        banknotes = {}
        if diff//500:
            banknotes[500] = diff//500
            diff %= 500
        if diff//100:
            banknotes[100] = diff//100
            diff %= 100
        if diff//50:
            banknotes[50] = diff//50
            diff %= 50
        if diff//20:
            banknotes[20] = diff//20
            diff %= 20
        if diff//10:
            banknotes[10] = diff//10
            diff %= 10
        if diff//5:
            banknotes[5] = diff//5
            diff %= 5
        if diff:
            banknotes[1] = diff
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

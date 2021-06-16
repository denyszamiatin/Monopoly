import settings


class Player:
    def __init__(self, name):
        self.name = name
        self.money = settings.START_MONEY
        self.field = 'GO'

    @property
    def all_money(self):
        """Sum all banknotes in player own and return it as integer."""
        money_sum = 0
        for i, j in self.money.items():
            money_sum += int(i) * j
        return money_sum


    def __str__(self):
        return f'player: {self.name}, with balance: {self.money} on field: {self.field}'

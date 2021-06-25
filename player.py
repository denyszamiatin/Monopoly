import settings
import utils

class Player:
    def __init__(self, name):
        self.name = name
        self.money = settings.START_MONEY
        self.field = 1

    @property
    def all_money(self):
        """Sum all banknotes in player own and return it as integer."""
        money_sum = 0
        for i, j in self.money.items():
            money_sum += int(i) * j
        return money_sum

    def move(self):
        """Move player on the field, according to his DICE roll."""
        self.field += utils.throw_dice()
        if self.field > 40:
            self.field -= 40

    def __str__(self):
        return f'player: {self.name}, with balance: {self.all_money} on field: {self.field}'

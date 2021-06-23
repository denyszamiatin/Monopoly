import settings
import random

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

    def throw_dice(self, quantity=2):
        """
        Throw the dice.
        :param quantity: Quantity of dice. Usually - 2.
        :return: List of integers from 1 to 6 as a result of dice roll.
        """
        return [random.randint(settings.DICE_MIN, settings.DICE_MAX) for _ in range(quantity)]

    def move(self):
        """Move player on the field, according to his DICE roll."""
        self.field += self.throw_dice()
        if self.field > 40:
            self.field -= 40

    def __str__(self):
        return f'player: {self.name}, with balance: {self.all_money} on field: {self.field}'

import settings
import money


class Player:
    def __init__(self, name):
        self.name = name
        self.balance = money.Money()
        self.field = settings.START_FIELD

    def move(self, dices):
        """Move player on the field, according to his DICE roll."""
        self.field = (self.field + dices) % settings.FIELDS_NUMBER

    def __str__(self):
        return f'player: {self.name}, with balance: {self.balance.total} on field: {self.field}'

    def __repr__(self):
        return f'Player({self.name})'

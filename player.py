import bank
import board


class Player:
    def __init__(self, name):
        self.name = name
        self.balance = bank.get_start_money()
        self.field = board.get_start_field()

    def move(self, dices):
        """Move player on the field, according to his DICE roll."""
        self.field = board.get_player_position(self.field, dices)

    def __str__(self):
        return f'player: {self.name}, with balance: {self.balance.total} on field: {self.field}'

    def __repr__(self):
        return f'Player({self.name})'

import settings
import money


class Player:
    def __init__(self, name, board):
        self.name = name
        self.balance = money.Money()
        self.play_board = board
        self.field = board.cells[settings.START_FIELD]

    def move(self, dices):
        """Move player on the field, according to his DICE roll."""
        new_field_index = (self.field.index + dices) % settings.FIELDS_NUMBER
        self.field = self.play_board.cells[new_field_index]

    def __str__(self):
        return f'player: {self.name}, with balance: {self.balance.total} on field: {self.field}'

    def __repr__(self):
        return f'Player({self.name})'

import bank
import board


class Player:
    def __init__(self, name):
        self.name = name
        self.balance = bank.get_start_money()
        self.field = board.get_start_field()

    def move(self, dices):
        """Move player on the field, according to his DICE roll."""
        start = self.field
        self.field = board.get_player_position(self.field, dices)
        board.fields[self.field].functionality(self)
        if 12 > self.field > 0 and 28 < start <= 39:
            board.fields[0].functionality(self)
        print(self)

    def pay_rent(self, other):  # TODO реализовать по другому Ишью.
        pass

    def buy(self, property_field):
        if self.balance < property_field.value:
            return False
        else:
            while True:
                choice = input('Do you want to buy? Y/N\n')
                if choice == 'Y':
                    self.balance -= property_field.value
                    property_field.owner = self
                    return True
                elif choice == 'N':
                    return False

    def __str__(self):
        return f'player: {self.name}, with balance: {self.balance.total}' \
               f' on field: {self.field}'

    def __repr__(self):
        return f'Player({self.name})'

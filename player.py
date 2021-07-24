import bank
import board


class Player:
    def __init__(self, name):
        self.name = name
        self.balance = bank.get_start_money()
        self.field = board.get_start_field()
        self.bankrupt = False

    def move(self, dices):
        """Move player on the field, according to his DICE roll."""
        start = self.field
        self.field = board.get_player_position(self.field, dices)
        board.fields[self.field].functionality(self)
        if 12 > self.field > 0 and 28 < start <= 39:
            board.fields[0].functionality(self)
        print(self)

    def pay_rent(self, owner, rent):
        assert isinstance(owner, Player), f'Type "Player" is expected,' \
                            f' got {type(owner)} instead!'
        if self.balance < rent:  # TODO реализовать залог.
            self.bankrupt = True
        else:
            self.balance -= rent
            owner.balance += rent

    def buy(self, value):
        if self.balance < value:
            return False
        while True:
            choice = input('Do you want to buy? Y/N\n').upper().strip()
            if choice == 'Y':
                self.balance -= value
                return True
            elif choice == 'N':
                return False

    def __str__(self):
        return f'player: {self.name}, with balance: {self.balance.total}' \
               f' on field: {self.field}'

    def __repr__(self):
        return f'Player({self.name})'

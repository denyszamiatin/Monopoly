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
        """Pay rent to another player."""
        assert isinstance(owner, Player), f'Type "Player" is expected,' \
                            f' got {type(owner)} instead!'
        if self.balance < rent:  # TODO реализовать залог.
            self.bankrupt = True
        else:
            self.balance -= rent
            owner.balance += rent

    def buy(self, value):
        """
        Choose to buy or not a property, if you have enough money.
        :param value:
        :return:
        """
        if self.balance < value:
            return False
        while True:
            choice = input('Do you want to buy? Y/N\n').upper().strip()
            if choice == 'Y':
                self.balance -= value
                return True
            elif choice == 'N':
                return False

    def bid(self, max_bid):
        """
        Make a bid during Auction.
        :param max_bid:
        :return:
        """
        while True:
            try:
                bid = int(input(f'''Player {self.name}, make a bid.
Now max is {max_bid}. If you want to quit the auction - type '0' '''))
                if bid == 0:
                    return 'PASS'
                elif bid <= max_bid:
                    print('Too small bid. Try again.')
                elif bid > self.balance.total:
                    print('You dont have this money!')
                else:
                    return bid
            except ValueError:
                print('Wrong input!!!')

    def __str__(self):
        return f'player: {self.name}, with balance: {self.balance.total}' \
               f' on field: {self.field}'

    def __repr__(self):
        return f'Player({self.name})'




import settings


class Player:
    def __init__(self, name):
        self.name = name
        self.money = settings.START_MONEY
        self.field = 'GO'

    def __str__(self):
        return f'player: {self.name}, with balance: {self.money} on field: {self.field}'

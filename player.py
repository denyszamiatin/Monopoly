import settings


class Player:
    def __init__(self, name):
        self.name = name
        self.money = settings.START_MONEY
        self.field = 'GO'

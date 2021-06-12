import settings


def input_players_qty():
    """
    Ask players quantity from user. Allowed 2-6 players.
    :return: Quantity of users as integer.
    """
    while True:
        try:
            qty = int(input(f'Enter player q-ty: {settings.MIN_PLAYERS_NUMBER}-{settings.MAX_PLAYERS_NUMBER}\n'))
            if settings.MIN_PLAYERS_NUMBER <= qty <= settings.MAX_PLAYERS_NUMBER:
                return qty
        except ValueError:
            pass
        print('Wrong q-ty!')


def input_player_names(quantity):
    return [input('What is your name? ') for _ in range(quantity)]


if __name__ == '__main__':
    players_qty = input_players_qty()
    players = input_player_names(players_qty)

def input_players_qty():
    """
    Function asks players quantity from user. Allowed 2-6 players.
    :return: Quantity of user as integer.
    """
    while True:
        qty = int(input(f'Enter player q-ty: 2-6\n'))
        if 7 > qty > 1:
            return qty
        else:
            print('Wrong q-ty!')

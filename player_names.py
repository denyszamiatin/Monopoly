def input_player_names(quantity):
    return [input('What is your name? ') for _ in range(quantity)]


players = input_player_names(3)  # TODO: argument is the variable from issue #1

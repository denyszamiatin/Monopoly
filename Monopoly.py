WELCOME_MESSAGE='Hello, and welcome to the game of Monopoly!\n'
MIN_PLAYERS=2
MAX_PLAYERS=8

print(WELCOME_MESSAGE)

while True:
    try:
        amount_of_players = int(input('Please tell me, how many players will join:'))
    except ValueError:
        print('Something is wrong!')
        continue
    if (amount_of_players<MIN_PLAYERS):
        print(f'You need at least {MIN_PLAYERS} players to play Monopoly.') 
        continue
    elif (amount_of_players>MAX_PLAYERS):
        print(f'Too many players, maximum amount of players to play Monopoly is {MAX_PLAYERS}')
        continue
    else:
        print(f'Great, {amount_of_players} it is!')
        break


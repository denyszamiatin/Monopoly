import players_list
import board


if __name__ == '__main__':
    players_list.players[0].move(1)
    for player in players_list.players:
        print(player)
    for field in board.fields:
        print(field)


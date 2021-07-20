import settings
import player
import utils
import bank
import board


def get_first_player(players: list[player.Player], throw_dice=utils.throw_dice):
    """
    Throws dices and returns address Pytest fixturesof the Player object who has the biggest value, if tie - called again.
    :param players: List of players - list of objects.
    :return: Address of Player object.
    """
    assert all(isinstance(x, player.Player) for x in players)
    winners = players.copy()
    while True:
        print('Rolling the dices!')
        first_dices = [utils.throw_dice() for _ in winners]
        for i, winner in enumerate(winners):
            print(f'{winner.name} rolled {first_dices[i]}')
        scores = [sum(i) for i in first_dices]
        max_score = max(scores)
        winners = [winner for i, winner in enumerate(winners) if scores[i] == max_score]

        if len(winners) == 1:
            return winners[0]


def sort_players(players: list[player.Player], first_player: player.Player):
    """
    Sorts player list so first player is first in the list.
    :param players: List of players - list of objects.
    :param first_player: Player object.
    :return: Sorted list of Player objects.
    """
    index = players.index(first_player)
    ordered_players = players[index:] + players[:index]
    print(f'Player order is : {",".join(item.name for item in ordered_players)}')
    return ordered_players


def input_players_qty() -> int:
    """
    Ask players quantity from user. Allowed from MIN_PLAYERS_NUMBER to MAX_PLAYERS_NUMBER from settings.
    :return: Quantity of players as integer.
    """
    while True:
        try:
            qty = int(input(f'Enter player q-ty: {settings.MIN_PLAYERS_NUMBER}-{settings.MAX_PLAYERS_NUMBER}\n'))
            if settings.MIN_PLAYERS_NUMBER <= qty <= settings.MAX_PLAYERS_NUMBER:
                return qty
        except ValueError:
            pass
        print('Wrong q-ty!')


def create_players(quantity: int) -> list[player.Player]:
    """
    Ask players names and create objects of class Player for each of them.
    :param play_board:
    :param quantity: Quantity of players for particular game - integer.
    :return: List of players.
    """
    return [player.Player(input('What is your name? ')) for _ in range(quantity)]


if __name__ == '__main__':
    players_qty = input_players_qty()
    players = create_players(players_qty)
    first_player = get_first_player(players)
    players = sort_players(players, first_player)
    for player in players:
        print(player)
    order = 0
    for field in board.fields:
        print(field)


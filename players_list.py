import utils
from player import Player
import settings
import money

def get_first_player(players):
    """
    Throws dices and returns address Pytest fixtures of
     the Player object who has the biggest value, if tie - called again.
    :param throw_dice:
    :param players: List of players - list of objects.
    :return: Address of Player object.
    """
    winners = players.copy()
    while True:
        print('Rolling the dices!')
        first_dices = [utils.throw_dice() for _ in winners]
        for i, winner in enumerate(winners):
            print(f'{winner.name} rolled {first_dices[i]}')
        scores = [sum(i) for i in first_dices]
        max_score = max(scores)
        winners = [winner for i, winner in enumerate(winners)
                   if scores[i] == max_score]

        if len(winners) == 1:
            return winners[0]


def sort_players(players, first_player):
    """
    Sorts player list so first player is first in the list.
    :param players: List of players - list of objects.
    :param first_player: Player object.
    :return: Sorted list of Player objects.
    """
    index = players.index(first_player)
    ordered_players = players[index:] + players[:index]
    print(f'Player order is: '
          f'{",".join(item.name for item in ordered_players)}')
    return ordered_players


def input_players_qty() -> int:
    """
    Ask players quantity from user.
    Allowed from MIN_PLAYERS_NUMBER to MAX_PLAYERS_NUMBER from settings.
    :return: Quantity of players as integer.
    """
    while True:
        try:
            qty = int(input(f'Enter player q-ty: {settings.MIN_PLAYERS_NUMBER}'
                            f'-{settings.MAX_PLAYERS_NUMBER}\n'))
            if settings.MIN_PLAYERS_NUMBER <= qty\
                    <= settings.MAX_PLAYERS_NUMBER:
                return qty
        except ValueError:
            pass
        print('Wrong q-ty!')


def create_players(quantity: int) -> list[Player]:
    """
    Ask players names and create objects of class Player for each of them.
    :param quantity: Quantity of players for particular game - integer.
    :return: List of players.
    """
    return [Player(input('What is your name? '))
            for _ in range(quantity)]


def auction():
    """An auction gives all players opportunity to buy a property.
     First bid is 1. Auction runs till 1 player."""
    player_auction = players.copy()
    max_bid = 1
    while len(player_auction) > 1:
        for player in player_auction:
            bid = player.bid(max_bid)
            if bid == "PASS":
                player_auction.remove(player)
            else:
                max_bid = bid
    auction_winner = player_auction[0]
    print(f'{player_auction[0]} has won an auction!')
    auction_winner.balance -= money.Money(money.divide_in_banknotes(max_bid))
    return auction_winner


players_qty = input_players_qty()
players = create_players(players_qty)
first_player = get_first_player(players)
players = sort_players(players, first_player)

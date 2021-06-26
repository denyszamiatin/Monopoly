import main
import player


def test_sort_players():
    A = player.Player('A')
    B = player.Player('B')
    C = player.Player('C')
    D = player.Player('D')
    players = [A, B, C, D]
    sorted_players = main.sort_players(players, players[2])
    assert sorted_players == [C, D, A, B]
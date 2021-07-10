import random
import unittest.mock

import pytest

import main
import player


@pytest.fixture(scope='module')
def A():
    return player.Player('A')


@pytest.fixture(scope='module')
def B():
    return player.Player('B')


@pytest.fixture(scope='module')
def C():
    return player.Player('C')


@pytest.fixture(scope='module')
def D():
    return player.Player('D')


def test_sort_players(A, B, C, D):
    players = [A, B, C, D]
    assert main.sort_players(players, C) == [C, D, A, B]


def test_sort_players_start(A, B, C, D):
    players = [A, B, C, D]
    assert main.sort_players(players, A) == [A, B, C, D]


def test_first_player_random(A, B, C, D):
    random.seed(1)
    assert main.get_first_player([A, B, C, D]) == D


# def test_first_player_predicted(A, B, C, D):
#     class TestDice:
#         def __init__(self):
#             self.i = 0
#             self.dices = ((1, 1), (2, 2), (3, 3), (4, 4))
#
#         def throw_dice(self):
#             self.i += 1
#             return self.dices[self.i - 1]
#
#     test_dice = TestDice()
#     assert main.get_first_player([A, B, C, D], throw_dice=test_dice.throw_dice) == D
#
#
# def test_first_player_predicted1(A, B, C, D):
#     class TestDice:
#         def __init__(self):
#             self.i = 0
#             self.dices = ((1, 1), (2, 2), (4, 4), (4, 4), (1, 1), (2, 2))
#
#         def throw_dice(self):
#             self.i += 1
#             return self.dices[self.i - 1]
#
#     test_dice = TestDice()
#     assert main.get_first_player([A, B, C, D], throw_dice=test_dice.throw_dice) == D


@unittest.mock.patch('utils.throw_dice')
def test_first_player_with_mocks(m: unittest.mock.Mock, A, B, C, D):
    m.side_effect = (1, 1), (2, 2), (3, 3), (4, 4)
    assert main.get_first_player([A, B, C, D]) == D


# @unittest.mock.patch('builtins.input', side_effect=['A', 'B', 'C', 'D'])
# def test_create_players1(mock):
#     assert main.create_players(4) == [player.Player('A'),player.Player('B'),
#                                       player.Player('C'),player.Player('D')]

@unittest.mock.patch('builtins.input')
def test_create_players_list(m: unittest.mock.Mock):
    m.side_effect = ['A', 'B', 'C', 'D']
    assert len(main.create_players(4)) == 4


@unittest.mock.patch('builtins.input')
def test_create_players_list2(m: unittest.mock.Mock):
    m.side_effect = ['A', 'B', 'C', 'D']
    assert len(main.create_players(2)) == 2


@unittest.mock.patch('builtins.input')
def test_create_players(m: unittest.mock.Mock):
    m.side_effect = ['A', 'B', 'C', 'D']
    players = main.create_players(4)
    assert [player.name for player in players] == ['A', 'B', 'C', 'D']


@unittest.mock.patch('builtins.input')
def test_input_players_qty_min(m: unittest.mock.Mock):
    m.side_effect = '2'
    assert main.input_players_qty() == 2


@unittest.mock.patch('builtins.input')
def test_input_players_qty_max(m: unittest.mock.Mock):
    m.side_effect = '6'
    assert main.input_players_qty() == 6


@unittest.mock.patch('builtins.input')
def test_input_players_qty_wrong_input(m: unittest.mock.Mock):
    m.side_effect = '1', '7', 'qwerty', '4'
    assert main.input_players_qty() == 4



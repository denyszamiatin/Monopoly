import pytest

import main
import player
import board


@pytest.fixture(scope='module')
def playing_board():
    return board.Board()


@pytest.fixture(scope='module')
def A(playing_board):
    return player.Player('A', playing_board)


@pytest.fixture(scope='module')
def B(playing_board):
    return player.Player('B', playing_board)


@pytest.fixture(scope='module')
def C(playing_board):
    return player.Player('C', playing_board)


@pytest.fixture(scope='module')
def D(playing_board):
    return player.Player('D', playing_board)


def test_sort_players(A, B, C, D):
    players = [A, B, C, D]
    assert main.sort_players(players, C) == [C, D, A, B]


def test_sort_players_start(A, B, C, D):
    players = [A, B, C, D]
    assert main.sort_players(players, A) == [A, B, C, D]

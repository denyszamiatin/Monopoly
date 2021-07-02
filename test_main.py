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

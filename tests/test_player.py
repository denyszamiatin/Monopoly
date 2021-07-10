import pytest
import player


@pytest.fixture()
def A():
    return player.Player('A')


def test_move_from_start(A):
    A.move(6)
    assert A.field == 6


def test_move(A):
    A.move(6)
    A.move(5)
    assert A.field == 11

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


def test_move_lap_salary(A):
    A.move(39)
    A.move(2)
    assert A.balance.total == 1700


def test_move_lap_salary_double(A):
    A.move(40)
    A.move(1)
    A.move(1)
    assert A.balance.total == 1700

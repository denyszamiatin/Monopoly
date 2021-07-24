import pytest
import unittest.mock
import player
import board
import money
import settings


@pytest.fixture()
def A():
    return player.Player('A')


@pytest.fixture()
def player_without_money():
    player_B = player.Player('B')
    player_B.balance = money.Money({})
    return player_B


@pytest.fixture()
def fields():
    return [board.get_field(i, field) for i, field in enumerate(settings.BOARD)]


@pytest.fixture()
def property_field(fields):
    return fields[1]


@unittest.mock.patch('builtins.input')
def test_move_from_start(m: unittest.mock.Mock, A):
    m.side_effect = ['N', 'N', 'N']
    A.move(6)
    assert A.field == 6


@unittest.mock.patch('builtins.input')
def test_move(m: unittest.mock.Mock, A):
    m.side_effect = ['N', 'N', 'N']
    A.move(6)
    A.move(5)
    assert A.field == 11


@unittest.mock.patch('builtins.input')
def test_move_lap_salary(m: unittest.mock.Mock, A, fields):
    m.side_effect = ['N', 'N', 'N']
    A.move(39)
    A.move(2)
    assert A.balance.total == 1700


@unittest.mock.patch('builtins.input')
def test_move_lap_salary_double(m: unittest.mock.Mock, A):
    m.side_effect = ['N', 'N', 'N']
    A.move(40)
    A.move(1)
    A.move(1)
    assert A.balance.total == 1700


@unittest.mock.patch('builtins.input')
def test_buy_1(m: unittest.mock.Mock, A, property_field):
    m.side_effect = 'Y'
    assert A.buy(property_field.value)


@unittest.mock.patch('builtins.input')
def test_buy_2(m: unittest.mock.Mock, A, property_field):
    m.side_effect = 'N'
    assert not A.buy(property_field.value)


def test_buy_3(player_without_money, property_field):
    assert not player_without_money.buy(property_field.value)


def test_buy_4(player_without_money, property_field):
    player_without_money.buy(property_field.value)
    assert property_field.owner is None


@unittest.mock.patch('builtins.input')
def test_buy_6(m: unittest.mock.Mock, A, property_field):
    m.side_effect = 'Y'
    A.buy(property_field.value)
    assert A.balance.total == 1440


@unittest.mock.patch('builtins.input')
def test_buy_7(m: unittest.mock.Mock, A, property_field):
    m.side_effect = 'N'
    A.buy(property_field.value)
    assert property_field.owner is None


@unittest.mock.patch('builtins.input')
def test_buy_9(m: unittest.mock.Mock, A, property_field):
    m.side_effect = 'N'
    A.buy(property_field.value)
    assert A.balance.total == 1500


def test_pay_rent_1(A, player_without_money, property_field):
    A.pay_rent(player_without_money, property_field.rent)
    assert A.balance.total == 1498


def test_pay_rent_2(A, player_without_money, property_field):
    A.pay_rent(player_without_money, property_field)
    assert player_without_money.balance.total == 2


def test_pay_rent_bankrupt(A, player_without_money, property_field):
    player_without_money.pay_rent(A, property_field)
    assert player_without_money.bankrupt


def test_pay_rent_bankrupt_2(A, player_without_money, property_field):
    player_without_money.pay_rent(A, property_field)
    assert A.balance.total == 1500

import money
import pytest


@pytest.fixture()
def money_01():
    return money.Money({500: 1, 100: 1, 50: 1, 20: 1, 10: 1, 1: 1})


@pytest.fixture()
def money_02():
    return money.Money({100: 1, 20: 1, 10: 1, 1: 2})


@pytest.fixture()
def money_03():
    return money.Money({100: 5, 50: 2, 20: 4, 10: 0, 1: 1})


def test_sub(money_01, money_02):
    new_money = money_01 - money_02
    assert new_money.total == 549


def test_sub_exception(money_01, money_02):
    with pytest.raises(ValueError):
        assert money_02 - money_01


def test_add(money_01, money_02):
    new_money = money_01 + money_02
    assert new_money.total == 813


def test_gt(money_01, money_02):
    assert money_01 > money_02


def test_lt(money_01, money_02):
    assert money_02 < money_01


def test_eq_true(money_01, money_03):
    assert money_01 == money_03


def test_eq_false(money_01, money_02):
    assert money_01 != money_02

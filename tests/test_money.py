import money
import pytest


@pytest.fixture(scope='module')
def money_01():
    return money.Money(five_hundred=1, one_hundred=1, fifty=1, twenty=1, ten=1, one=1)


@pytest.fixture(scope='module')
def money_02():
    return money.Money(five_hundred=0, one_hundred=1, fifty=0, twenty=1, ten=1, one=2)


@pytest.fixture(scope='module')
def money_03():
    return money.Money(five_hundred=0, one_hundred=5, fifty=2, twenty=4, ten=0, one=1)


def test_sub(money_01, money_02):
    money_01 - money_02
    assert money_01.total == 549


def test_sub_exception(money_01, money_02):
    with pytest.raises(ValueError):
        assert money_02 - money_01


def test_add(money_01, money_02):
    money_01 + money_02
    assert money_01.total == 681


def test_gt(money_01, money_02):
    assert money_01 > money_02


def test_lt(money_01, money_02):
    assert money_02 < money_01


def test_eq_true(money_01, money_03):
    assert money_01 == money_03


def test_eq_false(money_01, money_02):
    assert money_01 != money_02
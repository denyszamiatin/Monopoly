import bank
import money


def test_get_start_money():
    assert bank.get_start_money() == \
           money.Money({500: 2, 100: 2, 50: 2, 20: 6, 10: 5, 5: 5, 1: 5})


def test_get_lap_salary():
    assert bank.get_lap_salary() == money.Money({100: 2})

import bank
import money


def test_get_start_money():
    assert bank.get_start_money() == money.Money(five_hundred=2, one_hundred=2,
                                                 fifty=2, twenty=6, ten=5,
                                                 five=5, one=5)


def test_get_lap_salary():
    assert bank.get_lap_salary() == money.Money(one_hundred=2)

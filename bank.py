import money


def get_start_money():
    return money.Money(five_hundred=2, one_hundred=2, fifty=2, twenty=6, ten=5, five=5, one=5)


def get_lap_salary():
    return money.Money(one_hundred=2)

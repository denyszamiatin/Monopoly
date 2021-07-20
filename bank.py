import money


def get_start_money():
    return money.Money({500: 2, 100: 2, 50: 2, 20: 6, 10: 5, 5: 5, 1: 5})


def get_lap_salary():
    return money.Money({100: 2})

import money

class Bank:
    @staticmethod
    def get_start_money():
        value = money.Money(five_hundred=2, one_hundred=2, fifty=2, twenty=6, ten=5, five=5, one=5)
        return value

    @staticmethod
    def get_salary():
        value = money.Money(one_hundred=2)
        return value
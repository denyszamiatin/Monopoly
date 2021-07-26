import settings
import random
import bank
import money
import utils
import players_list


class Cards:
    def __init__(self, cards):
        self.cards = list(cards)
        random.shuffle(self.cards)

    def get_top_card(self):
        """Return top card from deck and shuffle it to bottom."""
        card = self.cards.pop(0)
        self.cards.append(card)
        return card


community_chest_cards = Cards(settings.COMMUNITY_CHEST_CARDS)
chance_cards = Cards(settings.CHANCE_CARDS)


class Field:
    def __init__(self, index, name):
        self.index = index
        self.name = name

    def __str__(self):
        return f'Field №{self.index}, name - {self.name}'


class PropertyField(Field):
    def __init__(self, index, name, color, value, rent_list):
        super().__init__(index, name)
        self.color = color
        self.value = money.Money(money.divide_in_banknotes(value))
        self.rent_list = rent_list
        self.owner = None
        self.mortgage = False
        self.buildings = []

    def get_owners(self):
        """Check who own all property of same color."""
        property_fields = [field for
                           field in fields if isinstance(field, PropertyField)]
        return [field.owner for
                        field in property_fields if self.color == field.color]

    def monopoly(self):
        """Check if property is in monopoly."""
        owners = self.get_owners()
        return len(set(owners)) == 1 and None not in owners

    @property
    def rent(self):
        """Return rent - sum of money to pay,
         if you stand on a property and dont own it"""
        if self.color == 'Utility':
            rent_coeff = self.rent_list[1] if self.monopoly() else self.rent_list[0]
            return rent_coeff * sum(utils.throw_dice())

        elif self.color == 'Railroad':
            own_qty = sum(owner == self.owner for owner in self.get_owners())
            return self.rent_list[own_qty - 1]

        else:
            rent = self.rent_list[0]
            if self.monopoly():
                rent *= 2
            if self.buildings:
                pass  # TODO Реализовать дома и отели позже.
            return rent

    def __str__(self):
        return f'Field №{self.index}, name - {self.name},' \
               f' color - {self.color},' \
               f' value - {self.value.total},' \
               f' owner - {self.owner}'

    def functionality(self, player):
        """
        1) If property is not owned yet - let player buy it. If he refuses
        auction starts.
        2) If property is owned buy another player. Pay rent to an owner.
        :param player:
        :return:
        """
        if self.owner is None:
            if player.buy(self.value):
                self.owner = player
            else:
                print(f'Auction is started! {self.name} is being sold.')
                self.owner = players_list.auction()
        elif self.owner != player:
            if not self.mortgage:  # TODO реализовать залоги.
                player.pay_rent(self.owner, money.divide_in_banknotes(self.rent))


class CardField(Field):
    def __init__(self, index, name, cards):
        super().__init__(index, name)
        self.cards = cards

    def functionality(self, player):
        print(self.cards.get_top_card())


class TaxField(Field):
    def __init__(self, index, name, tax):
        super().__init__(index, name)
        self.tax = money.Money(money.divide_in_banknotes(tax))

    def __str__(self):
        return f'Field №{self.index}, name - {self.name},' \
               f' tax - {self.tax.total}'

    def functionality(self, player):
        pass


class GoField(Field):
    def functionality(self, player):
        player.balance += bank.get_lap_salary()


class JailField(Field):
    def functionality(self, player):
        pass


class GoToJailField(Field):
    def functionality(self, player):
        pass


def get_field(number, field):
    field_type, *data = field
    if field_type == 'Property':
        return PropertyField(number, *data)
    elif field_type == 'GO':
        return GoField(number, field_type)
    elif field_type == 'Community Chest':
        return CardField(number, field_type, community_chest_cards)
    elif field_type == 'Tax':
        return TaxField(number, *data)
    elif field_type == 'Chance':
        return CardField(number, field_type, chance_cards)
    elif field_type == 'Jail':
        return JailField(number, field_type)
    elif field_type == 'Go to jail':
        return GoToJailField(number, field_type)
    elif field_type == 'Free Parking':
        return Field(number, field_type)
    else:
        raise AssertionError


def get_start_field():
    return 0


def get_player_position(current, offset):
    return (current + offset) % len(fields)


fields = [get_field(i, field) for i, field in enumerate(settings.BOARD)]

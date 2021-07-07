import settings


class Field:
    def __init__(self, index, name):
        self.index = index
        self.name = name

    def __str__(self):
        return f'Field №{self.index}, name - {self.name}'


class PropertyField(Field):
    def __init__(self, index, name, color, value):
        super().__init__(index, name)
        self.color = color
        self.value = value

    def __str__(self):
        return f'Field №{self.index}, name - {self.name},' \
               f' color - {self.color},' \
               f' value - {self.value}'

    def functionality(self):
        pass


class CommunityChestField(Field):
    __cards = settings.COMMUNITYCHESTCARDS

    def shuffle_card(self):
        """Take top card from deck and shuffle it to bottom."""
        CommunityChestField.__cards = CommunityChestField.__cards[1:] + \
                                      CommunityChestField.__cards[:0]

    def get_card(self):
        """Return top card from deck and shuffle it to bottom."""
        card = CommunityChestField.__cards[0]
        self.shuffle_card()
        print(card)
        return card


class ChanceField(Field):
    def functionality(self):
        pass


class TaxField(Field):
    def __init__(self, index, name, tax):
        super().__init__(index, name)
        self.tax = tax

    def __str__(self):
        return f'Field №{self.index}, name - {self.name},' \
               f' tax - {self.tax}'

    def functionality(self):
        pass


class GoField(Field):
    def functionality(self):
        pass


class JailField(Field):
    def functionality(self):
        pass


class GoToJailField(Field):
    def functionality(self):
        pass


def get_field(number, field):
    field_type, *data = field
    if field_type == 'Property':
        return PropertyField(number, *data)
    elif field_type == 'GO':
        return GoField(number, field_type)
    elif field_type == 'Community Chest':
        return CommunityChestField(number, field_type)
    elif field_type == 'Tax':
        return TaxField(number, *data)
    elif field_type == 'Chance':
        return ChanceField(number, field_type)
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

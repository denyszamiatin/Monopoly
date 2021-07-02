import settings


class BoardCell:
    def __init__(self, index, name):
        self.index = index
        self.name = name


class PropertyBoardCell(BoardCell):
    def __init__(self, index, name, color=None, value=None):
        super().__init__(index, name)
        self.color = color
        self.value = value

    def functionality(self):
        pass


class CommunityChestBoardCell(BoardCell):
    def functionality(self):
        pass


class ChanceBoardCell(BoardCell):
    def functionality(self):
        pass


class TaxBoardCell(BoardCell):
    def __init__(self, index, name, tax):
        super().__init__(index, name)
        self.tax = tax

    def functionality(self):
        pass


class GoBoardCell(BoardCell):
    def functionality(self):
        pass


class JailBoardCell(BoardCell):
    def functionality(self):
        pass


class GoToJailBoardCell(BoardCell):
    def functionality(self):
        pass


def get_cell(number, field):
    field_type, *data = field
    if field_type == 'Property':
        return PropertyBoardCell(number, *data)
    elif field_type == 'GO':
        return GoBoardCell(number, field_type)
    elif field_type == 'Community Chest':
        return CommunityChestBoardCell(number, field_type)
    elif field_type == 'Tax':
        return TaxBoardCell(number, *data)
    elif field_type == 'Chance':
        return ChanceBoardCell(number, field_type)
    elif field_type == 'Jail':
        return JailBoardCell(number, field_type)
    elif field_type == 'Go to jail':
        return GoToJailBoardCell(number, field_type)
    elif field_type == 'Free Parking':
        return BoardCell(number, field_type)
    else:
        raise AssertionError


def get_start_field():
    return 0


def get_player_position(current, offset):
    return (current + offset) % len(fields)


fields = [get_cell(i, field) for i, field in enumerate(settings.BOARD)]

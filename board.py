import settings


class BoardCell:
    def __init__(self, index, name, color=None, value=None):
        self.index = index
        self.name = name
        self.color = color
        self.value = value


class PropertyBoardCell(BoardCell):
    def functionality(self):
        pass


class CommunityChestBoardCell(BoardCell):
    def functionality(self):
        pass


class ChanceBoardCell(BoardCell):
    def functionality(self):
        pass


class TaxBoardCell(BoardCell):
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


class Board:
    def __init__(self):
        self.cells = []
        for i, k in enumerate(settings.BOARD):
            if k[0] == 'Property':
                self.cells.append(PropertyBoardCell(i, *k[1:]))
            elif k[0] == 'GO':
                self.cells.append(GoBoardCell(i, k[0]))
            elif k[0] == 'Community Chest':
                self.cells.append(CommunityChestBoardCell(i, k[0]))
            elif k[0] == 'Tax':
                self.cells.append(TaxBoardCell(i, *k[1:]))
            elif k[0] == 'Chance':
                self.cells.append(ChanceBoardCell(i, k[0]))
            elif k[0] == 'Jail':
                self.cells.append(JailBoardCell(i, k[0]))
            elif k[0] == 'Go to jail':
                self.cells.append(GoToJailBoardCell(i, k[0]))
            elif k[0] == 'Free Parking':
                self.cells.append(BoardCell(i, k[0]))

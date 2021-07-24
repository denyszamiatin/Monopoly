import pytest
import unittest.mock
import board
import player
import settings


@pytest.fixture()
def fields():
    return [board.get_field(i, field) for i, field in enumerate(settings.BOARD)]


@pytest.fixture()
def dice():
    return 6


@pytest.fixture()
def Q():
    return player.Player('Q')


@pytest.fixture()
def W():
    return player.Player('W')


@pytest.fixture()
def GO(fields):
    return fields[0]


@pytest.fixture()
def mediterranean_avenue(fields):
    return fields[1]


@pytest.fixture()
def baltic_avenue(fields):
    return fields[3]


def test_get_field_property():
    field = board.get_field(1, ('Property', 'Mediterranean Avenue',
                                'Purple', 60, [2, 10, 30, 90, 160, 250]))
    assert isinstance(field, board.PropertyField)


def test_get_field_tax():
    field = board.get_field(1, ('Tax', 'Income tax', 75))
    assert isinstance(field, board.TaxField)


def test_get_field_go():
    field = board.get_field(1, ('GO',))
    assert isinstance(field, board.GoField)


def test_get_field_error():
    with pytest.raises(AssertionError):
        board.get_field(1, ('Some field', 'LALALALA', 'Purple', 60))


def test_get_player_position_1(dice):
    assert board.get_player_position(1, dice) == 7


def test_get_player_position_39(dice):
    assert board.get_player_position(39, dice) == 5


def test_get_start_field():
    assert board.get_start_field() == 0


def test_go_functionality(Q, GO):
    GO.functionality(Q)
    assert Q.balance.total == 1700


@unittest.mock.patch('player.Player.buy')
def test_property_field_functionality(m: unittest.mock.Mock, baltic_avenue, Q):
    m.return_value = True
    baltic_avenue.functionality(Q)
    assert baltic_avenue.owner == Q


def test_property_rent_1(baltic_avenue):
    assert baltic_avenue.rent == 4


def test_property_rent_2(fields, Q):
    board.fields = fields
    fields[5].owner = Q
    assert fields[5].rent == 25


@unittest.mock.patch('utils.throw_dice')
def test_property_rent_3(m: unittest.mock.Mock, fields):
    m.return_value = (2, 2)
    assert fields[12].rent == 16


def test_property_monopoly(fields, Q):
    board.fields = fields
    fields[3].owner = Q
    fields[1].owner = Q
    assert fields[3].monopoly()


@unittest.mock.patch('board.PropertyField.monopoly')
def test_property_rent_monopoly(m: unittest.mock.Mock, baltic_avenue):
    m.return_value = True
    assert baltic_avenue.rent == 8

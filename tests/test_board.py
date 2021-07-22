import pytest
import board
import player
import bank


@pytest.fixture(scope='module')
def dice():
    return 6


@pytest.fixture()
def A():
    return player.Player('A')


@pytest.fixture()
def GO():
    return board.get_field(1, ('GO',))


def test_get_field_property():
    field = board.get_field(1, ('Property', 'Mediterranean Avenue',
                                'Purple', 60))
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


def test_GO_functionality(A, GO):
    GO.functionality(A)
    assert A.balance.total == 1700

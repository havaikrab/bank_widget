import pytest


@pytest.fixture
def card_number_too_short():
    return 1029384756


@pytest.fixture
def card_number_too_long():
    return 1022033304444055555066666607777777


@pytest.fixture
def card_number_empty():
    return None


@pytest.fixture
def card_number_invalid():
    return '1234567890qwerty'


@pytest.fixture
def card_number_float():
    return 1234567890.12345


@pytest.fixture
def account_too_short():
    return 12345


@pytest.fixture
def account_too_long():
    return 10220333044440555550666666077777770888888880999999999


@pytest.fixture
def account_empty():
    return None


@pytest.fixture
def account_invalid():
    return '1234567890qwerty'


@pytest.fixture
def account_float():
    return 1234567890.12345

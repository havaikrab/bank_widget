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

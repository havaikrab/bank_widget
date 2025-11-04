import pytest


@pytest.fixture
def card_number_standart():
    return 1234567890098765

@pytest.fixture
def card_number_short():
    return 9876543210

@pytest.fixture
def card_number_long():
    return 122333444455555666666

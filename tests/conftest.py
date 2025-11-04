import pytest


@pytest.fixture
def card_number_standard():
    return int(1022033304444055555)

@pytest.fixture
def card_number_short():
    return int(1029384756102)

@pytest.fixture
def card_number_long():
    return int(6668884442221113335)


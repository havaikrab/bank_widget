import pytest


@pytest.fixture
def card_number_too_short():
    return "1029384756"


@pytest.fixture
def card_number_too_long():
    return "1022033304444055555066666607777777"


@pytest.fixture
def card_number_empty():
    return None


@pytest.fixture
def card_number_invalid():
    return 1234567890


@pytest.fixture
def account_too_short():
    return "12345"


@pytest.fixture
def account_too_long():
    return "10220333044440555550666666077777770888888880999999999"


@pytest.fixture
def account_empty():
    return None


@pytest.fixture
def account_invalid():
    return 1234567890


@pytest.fixture
def requisites_invalid():
    return ["Visa Gold", 1234567890]


@pytest.fixture
def requisites_empty():
    return None


@pytest.fixture
def no_type_requisites():
    return "12313524357468585"


@pytest.fixture
def no_number_requisites():
    return "Visa Platinum"


@pytest.fixture
def requisites_wrong_sequence():
    return "1234567890123456 Visa Platinum"


@pytest.fixture
def requisites_mixed():
    return "Visa12345678Gold90123456"


@pytest.fixture
def requisites_unexpected_symbols():
    return "Счет №09876543210987654321"


@pytest.fixture
def requisites_too_long_number():
    return "Счёт 10220333044440555550666666077777770888888880999999999"


@pytest.fixture
def requisites_too_short_number():
    return "Счёт 1234567890"


@pytest.fixture
def log_empty():
    return None


@pytest.fixture
def log_invalid_type():
    return {"Day": "12", "Month": "12", "Year": "2012"}

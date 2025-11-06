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
def log_no_arg():
    return None


@pytest.fixture
def log_invalid_type():
    return {"Day": "12", "Month": "12", "Year": "2012"}


@pytest.fixture
def log_str_empty():
    return ''


@pytest.fixture
def dicts_list_no_arg():
    return None


@pytest.fixture
def dicts_list_invalid_type():
    return ({'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 698729329, 'state': 'PROCESSED', 'date': '2023-12-12T05:48:55.344688'},
            {'id': 89223248, 'state': 'CANCELED', 'date': '2005-01-12T21:16:25.247425'},
            {'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-03T23:27:01.533689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2019-10-14T08:21:33.419441'})

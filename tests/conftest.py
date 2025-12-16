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
def card_number_invalid_type():
    return 1234567890


@pytest.fixture
def card_number_incorrect():
    return "1234567890oo"


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
def account_invalid_type():
    return 1234567890


@pytest.fixture
def account_incorrect():
    return "1234567890oo"


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
    return ""


@pytest.fixture
def dicts_list_no_arg():
    return None


@pytest.fixture
def dicts_list_invalid_type():
    return (
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 698729329, "state": "PROCESSED", "date": "2023-12-12T05:48:55.344688"},
        {"id": 89223248, "state": "CANCELED", "date": "2005-01-12T21:16:25.247425"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-03T23:27:01.533689"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-10-14T08:21:33.419441"},
    )


@pytest.fixture
def some_dirty_transactions():
    return [
        ["operationAmount"],
        {
            "id": "CORRECT TRANSACTION",
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 'INVALID KEY "operationAmount"',
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "OOOperationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 'INVALID KEY "currency"',
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "CCCurrency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 'INVALID KEY "code"',
            "state": "EXECUTED",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "CCCode": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": "CORRECT TRANSACTION",
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def empty_transactions_list():
    return []


@pytest.fixture
def transactions_invalid_type():
    return {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }


@pytest.fixture
def card_number_invalid_start_type():
    return "10"


@pytest.fixture
def card_number_correct_type():
    return 30


@pytest.fixture
def card_number_invalid_stop_type():
    return [99]


@pytest.fixture
def transaction_invalid_date():
    return {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018*08*19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
    }

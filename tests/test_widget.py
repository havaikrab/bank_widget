import pytest

from src import widget


@pytest.mark.parametrize(
    "requisites, expected_mask",
    [
        ("Maestro   1596  8378  6870 5199", "Maestro 1596 83** **** 5199"),
        ("  СчЁт   64686473678894779589", "Счет **9589"),
        ("MasterCard 7158    3007 34 7 26 758  ", "MasterCard 7158 30** **** 6758"),
        ("сЧЕТ 35383033474447895560   ", "Счет **5560"),
        ("Visa       Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("          Visa Platinum   8990    9221    1366    5229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("СЧЕТ 7365 4108 4301 3587 4305", "Счет **4305"),
        ("  Some   UNKNOWN   Card    0001000200030004000", "Some UNKNOWN Card 0001 00** **** 4000"),
    ],
)
def test_mask_account_card(requisites, expected_mask):
    assert widget.mask_account_card(requisites) == expected_mask


def test_mask_account_card_invalid_type(requisites_invalid):
    with pytest.raises(TypeError):
        widget.mask_account_card(requisites_invalid)


def test_mask_account_card_empty(requisites_empty):
    with pytest.raises(TypeError):
        widget.mask_account_card(requisites_empty)


def test_mask_account_card_no_type(no_type_requisites):
    with pytest.raises(ValueError):
        widget.mask_account_card(no_type_requisites)


def test_mask_account_card_no_number(no_number_requisites):
    with pytest.raises(ValueError):
        widget.mask_account_card(no_number_requisites)


def test_mask_account_card_wrong_sequence(requisites_wrong_sequence):
    with pytest.raises(ValueError):
        widget.mask_account_card(requisites_wrong_sequence)


def test_mask_account_card_mixed_requisites(requisites_mixed):
    with pytest.raises(ValueError):
        widget.mask_account_card(requisites_mixed)


def test_mask_account_card_unexpected_symbols(requisites_unexpected_symbols):
    with pytest.raises(ValueError):
        widget.mask_account_card(requisites_unexpected_symbols)


def test_mask_account_card_too_long_number(requisites_too_long_number):
    with pytest.raises(ValueError):
        widget.mask_account_card(requisites_too_long_number)


def test_mask_account_card_too_short_number(requisites_too_short_number):
    with pytest.raises(ValueError):
        widget.mask_account_card(requisites_too_short_number)


@pytest.mark.parametrize(
    "detailed_log, expected_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2999-12-31T23:59:59.999999", "31.12.2999"),
        ("1988-10-04T08:50:11.1", "04.10.1988"),
        ("4123-01-12T00:00:00.0", "12.01.4123"),
        ("9999-12-31T23:59:59.999999", "31.12.9999"),
    ],
)
def test_get_date(detailed_log, expected_date):
    assert widget.get_date(detailed_log) == expected_date


def test_get_date_no_arg(log_no_arg):
    with pytest.raises(TypeError):
        widget.get_date(log_no_arg)


def test_get_date_invalid_type(log_invalid_type):
    with pytest.raises(TypeError):
        widget.get_date(log_invalid_type)


def test_get_date_str_empty(log_str_empty):
    with pytest.raises(ValueError):
        widget.get_date(log_str_empty)


@pytest.mark.parametrize(
    "invalid_log",
    [
        "24-03-11T02:26:18.671407",
        "2024-3-11T02:26:18.671407",
        "2o24-o3-11T02:26:18.671407",
        "2024_12_11T02:26:18.671407",
    ],
)
def test_get_date_invalid_format(invalid_log):
    assert widget.get_date(invalid_log) == ""

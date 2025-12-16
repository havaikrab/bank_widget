from unittest.mock import mock_open, patch

import pytest

from src import utils


mock_data = mock_open(read_data='[{"id": 123, "currency": {"code": "RUB", "amount": 1000}}]')


@patch("builtins.open", mock_data)
def test_get_transactions():
    assert utils.get_transactions("data/operations.json") == [{"id": 123, "currency": {"code": "RUB", "amount": 1000}}]
    mock_data.assert_called_once_with("data/operations.json", "r", encoding="utf-8")


mock_invalid_data = mock_open(read_data='{"id": 123, "currency": {"code": "RUB", "amount": 1000}}')


@patch("builtins.open", mock_invalid_data)
def test_get_transactions_invalid_data():
    assert utils.get_transactions("data/operations.json") == []
    mock_data.assert_called_once_with("data/operations.json", "r", encoding="utf-8")


def test_get_transactions_no_datafile():
    assert utils.get_transactions("data/file_not_found.txt") == []


@pytest.mark.parametrize(
    "transaction_dict, expected_value",
    [
        (
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            },
            31957.58,
        ),
        (
            {
                "id": 587085106,
                "state": "EXECUTED",
                "date": "2018-03-23T10:45:06.972075",
                "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            },
            48223.05,
        ),
        (
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            },
            43318.34,
        ),
    ],
)
def test_get_amount_rubles(transaction_dict, expected_value):
    assert utils.get_amount_rubles(transaction_dict) == expected_value


@pytest.mark.parametrize(
    "transaction_dict",
    [
        (
            [
                {
                    "id": "INVALID TRANSACTION TYPE",
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                }
            ]
        ),
        (
            {
                "id": "INVALID DATE KEY",
                "state": "EXECUTED",
                "DATE": "2018-03-23T10:45:06.972075",
                "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            }
        ),
        (
            {
                "id": "INVALID OPERATIONAMOUNT KEY",
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "OPERATIONAMOUNT": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            }
        ),
        (
            {
                "id": "INVALID AMOUNT KEY",
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"AMOUNT": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            }
        ),
        (
            {
                "id": "INVALID CURRENCY KEY",
                "state": "EXECUTED",
                "date": "2018-12-20T16:43:26.929246",
                "operationAmount": {"amount": "70946.18", "CURRENCY": {"name": "USD", "code": "USD"}},
            }
        ),
        (
            {
                "id": "INVALID CODE KEY",
                "state": "EXECUTED",
                "date": "2019-07-12T20:41:47.882230",
                "operationAmount": {"amount": "51463.70", "currency": {"name": "USD", "CODE": "USD"}},
            }
        ),
    ],
)
def test_get_amount_rubles_invalid_keys(transaction_dict):
    with pytest.raises(ValueError):
        utils.get_amount_rubles(transaction_dict)


def test_get_amount_rubles_invalid_date(transaction_invalid_date):
    with pytest.raises(KeyError):
        utils.get_amount_rubles(transaction_invalid_date)


@patch("src.external_api.get_currency_rate_by_date")
def test_get_amount_rubles_external_request(mocked_rate):
    mocked_rate.return_value = {"status": True, "rate": 0.01}
    assert (
        utils.get_amount_rubles(
            {
                "id": 522357576,
                "state": "EXECUTED",
                "date": "2019-07-12T20:41:47.882230",
                "operationAmount": {"amount": "123.45", "currency": {"name": "USD", "code": "USD"}},
            }
        )
        == 12345.0
    )
    mocked_rate.assert_called_once_with("USD", "2019-07-12")


@patch("src.external_api.get_currency_rate_by_date")
def test_get_amount_rubles_unknown_currency_code(mocked_rate, capsys):
    mocked_rate.return_value = {"status": True, "rate": None}
    utils.get_amount_rubles(
        {
            "id": 522357576,
            "state": "EXECUTED",
            "date": "2019-07-12T20:41:47.882230",
            "operationAmount": {"amount": "123.45", "currency": {"name": "Евро", "code": "Euro"}},
        }
    )
    captured = capsys.readouterr()
    assert captured.out == "Неизвестный код валюты транзакции\n"
    assert (
        utils.get_amount_rubles(
            {
                "id": 522357576,
                "state": "EXECUTED",
                "date": "2019-07-12T20:41:47.882230",
                "operationAmount": {"amount": "123.45", "currency": {"name": "Евро", "code": "Euro"}},
            }
        )
        == 0.0
    )
    mocked_rate.assert_called_with("Euro", "2019-07-12")


@patch("src.external_api.get_currency_rate_by_date")
def test_get_amount_rubles_bad_rate_status(mocked_rate, capsys):
    mocked_rate.return_value = {"status": False, "rate": None}
    utils.get_amount_rubles(
        {
            "id": 522357576,
            "state": "EXECUTED",
            "date": "2019-07-12T20:41:47.882230",
            "operationAmount": {"amount": "123.45", "currency": {"name": "Евро", "code": "Euro"}},
        }
    )
    assert (
        utils.get_amount_rubles(
            {
                "id": 522357576,
                "state": "EXECUTED",
                "date": "2019-07-12T20:41:47.882230",
                "operationAmount": {"amount": "123.45", "currency": {"name": "Евро", "code": "Euro"}},
            }
        )
        == 0.0
    )
    mocked_rate.assert_called_with("Euro", "2019-07-12")

import os
from unittest.mock import patch

from dotenv import load_dotenv

from src import external_api


@patch("requests.get")
def test_get_currency_rate_by_date(mock_get):
    load_dotenv()
    api_key = os.getenv("exchangerates_API_KEY")
    test_headers = {"apikey": api_key}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "date": "2022-11-11",
        "quotes": {"RUBEUR": 0.015923, "RUBUSD": 0.016515},
        "source": "RUB",
    }
    assert external_api.get_currency_rate_by_date("USD", "2022-11-11") == {"status": True, "rate": 0.016515}
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/currency_data/historical?date=2022-11-11&source=RUB", headers=test_headers
    )


@patch("requests.get")
def test_get_currency_rate_by_date_unauthorized(mock_get, capsys):
    load_dotenv()
    api_key = os.getenv("exchangerates_API_KEY")
    test_headers = {"apikey": api_key}
    mock_get.return_value.status_code = 401

    external_api.get_currency_rate_by_date("USD", "2022-11-11")
    captured = capsys.readouterr()
    assert captured.out == "Для обращения к внешней базы данных необходима аутентификация пользователя\n"
    assert external_api.get_currency_rate_by_date("USD", "2022-11-11") == {"status": False, "rate": None}
    mock_get.assert_called_with(
        "https://api.apilayer.com/currency_data/historical?date=2022-11-11&source=RUB", headers=test_headers
    )


@patch("requests.get", side_effect=Exception("Bad Connection"))
def test_get_currency_rate_by_date_bad_connection(mock_get, capsys):
    load_dotenv()
    api_key = os.getenv("exchangerates_API_KEY")
    test_headers = {"apikey": api_key}
    with mock_get.raises(Exception):
        external_api.get_currency_rate_by_date("USD", "2022-11-11")
        captured = capsys.readouterr()
        assert captured.out == "Нестабильное подключение к сети или внешняя база данных временно недоступна\n"
        assert external_api.get_currency_rate_by_date("USD", "2022-11-11") == {"status": False, "rate": None}
        mock_get.assert_called_with(
            "https://api.apilayer.com/currency_data/historical?date=2022-11-11&source=RUB", headers=test_headers
        )

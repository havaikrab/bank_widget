from unittest.mock import mock_open, patch

import pandas as pd

from src import data_readers


mock_empty_data = mock_open(read_data="")
mock_invalid_data = mock_open(read_data="***")
first_string = "id;state;date;amount;currency_name;currency_code;from;to;description\n"
second_string_one = "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;"
second_string_two = "Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n"
third_string_one = "3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;"
third_string_two = "Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту\n"
mock_data = mock_open(
    read_data=(first_string + second_string_one + second_string_two + third_string_one + third_string_two)
)

empty_data_frame = pd.DataFrame()
invalid_data_frame = pd.DataFrame({"кошечки": ["Муся", "Пуся", "Дуся"], "собачки": ["Тузик", "Шарик", "Коржик"]})

data_frame = pd.DataFrame(
    {
        "id": [650703, 3598919, 593027],
        "state": ["EXECUTED", "EXECUTED", "CANCELED"],
        "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z", "2023-07-22T05:02:01Z"],
        "amount": [16210, 29740, 30368],
        "currency_name": ["Sol", "Peso", "Shilling"],
        "currency_code": ["PEN", "COP", "TZS"],
        "from": ["Счет 58803664561298323391", "Discover 3172601889670065", "Visa 1959232722494097"],
        "to": ["Счет 39745660563456619397", "Discover 0720428384694643", "Visa 6804119550473710"],
        "description": ["Перевод организации", "Перевод с карты на карту", "Перевод с карты на карту"],
    }
)


def test_csv_data_reader_no_datafile():
    assert data_readers.csv_data_reader("data/file_not_found.csv") == []


@patch("builtins.open", mock_empty_data)
def test_csv_data_reader_empty():
    assert data_readers.csv_data_reader("data/empty_data.csv") == []
    mock_empty_data.assert_called_once_with("data/empty_data.csv", "r", encoding="utf-8")


@patch("builtins.open", mock_invalid_data)
def test_csv_data_reader_invalid():
    assert data_readers.csv_data_reader("data/invalid_data.csv") == []
    mock_invalid_data.assert_called_with("data/invalid_data.csv", "r", encoding="utf-8", errors="strict", newline="")


@patch("builtins.open", mock_data)
def test_csv_data_reader():
    assert data_readers.csv_data_reader("data/data.csv") == [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {"amount": 16210, "currency": {"name": "Sol", "code": "PEN"}},
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": 3598919,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "operationAmount": {"amount": 29740, "currency": {"name": "Peso", "code": "COP"}},
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
    ]
    mock_data.assert_called_with("data/data.csv", "r", encoding="utf-8", errors="strict", newline="")


def test_xlsx_data_reader_no_datafile():
    assert data_readers.xlsx_data_reader("data/file_not_found.xlsx") == []


@patch("pandas.read_excel")
def test_xlsx_data_reader_empty(mock_read_excel):
    mock_read_excel.return_value = empty_data_frame
    assert data_readers.xlsx_data_reader("data/empty_data.xlsx") == []
    mock_read_excel.assert_called_once_with("data/empty_data.xlsx")


@patch("pandas.read_excel")
def test_xlsx_data_reader_invalid(mock_read_excel):
    mock_read_excel.return_value = invalid_data_frame
    assert data_readers.xlsx_data_reader("data/invalid_data.xlsx") == []
    mock_read_excel.assert_called_once_with("data/invalid_data.xlsx")


@patch("pandas.read_excel")
def test_xlsx_data_reader(mock_read_excel):
    mock_read_excel.return_value = data_frame
    assert data_readers.xlsx_data_reader("data/data.xlsx") == [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {"amount": 16210, "currency": {"name": "Sol", "code": "PEN"}},
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": 3598919,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "operationAmount": {"amount": 29740, "currency": {"name": "Peso", "code": "COP"}},
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
        {
            "id": 593027,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "operationAmount": {"amount": 30368, "currency": {"name": "Shilling", "code": "TZS"}},
            "description": "Перевод с карты на карту",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
        },
    ]
    mock_read_excel.assert_called_once_with("data/data.xlsx")

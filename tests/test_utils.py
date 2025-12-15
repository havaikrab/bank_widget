import pytest
from src import utils
from unittest.mock import patch, mock_open

mock_data = mock_open(read_data='[{"id": 123, "currency": {"code": "RUB", "amount": 1000}}]')

@patch('builtins.open', mock_data)
def test_get_transactions():
    assert utils.get_transactions('data/operations.json') == [{"id": 123, "currency": {"code": "RUB", "amount": 1000}}]
    mock_data.assert_called_once_with('data/operations.json', 'r', encoding='utf-8')


mock_invalid_data = mock_open(read_data='{"id": 123, "currency": {"code": "RUB", "amount": 1000}}')

@patch('builtins.open', mock_invalid_data)
def test_get_transactions_invalid_data():
    assert utils.get_transactions('data/operations.json') == []
    mock_data.assert_called_once_with('data/operations.json', 'r', encoding='utf-8')

def test_get_transactions_no_datafile():
    assert utils.get_transactions('data/file_not_found.txt') == []
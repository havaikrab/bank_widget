import pytest

from src import widget

from src import masks

@pytest.mark.parametrize('requisites, expected_mask', [('Maestro   1596  8378  6870 5199', 'Maestro 1596 83** **** 5199'),
                                                       ('  СчЁт   64686473678894779589', 'Счет **9589'),
                                                       ('MasterCard 7158    3007 34 7 26 758  ', 'MasterCard 7158 30** **** 6758'),
                                                       ('сЧЕТ 35383033474447895560   ', 'Счет **5560'),
                                                       ('Visa       Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
                                                       ('          Visa Platinum   8990    9221    1366    5229', 'Visa Platinum 8990 92** **** 5229'),
                                                       ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
                                                       ('СЧЕТ 7365 4108 4301 3587 4305', 'Счет **4305'),
                                                       ('  Some   UNKNOWN   Card    0001000200030004000', 'Some UNKNOWN Card 0001 00** **** 4000')])

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

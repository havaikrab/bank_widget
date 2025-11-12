import pytest

from src import masks


@pytest.mark.parametrize(
    "card_number, expected_mask",
    [
        ("1234567890098765", "1234 56** **** 8765"),
        ("9988776543210", "9988 77** **** 3210"),
        ("1223334444555556666", "1223 33** **** 6666"),
    ]
)
def test_get_mask_card_number(card_number, expected_mask):
    assert masks.get_mask_card_number(card_number) == expected_mask


def test_get_mask_card_too_short_number(card_number_too_short):
    with pytest.raises(ValueError):
        masks.get_mask_card_number(card_number_too_short)


def test_get_mask_card_too_long_number(card_number_too_long):
    with pytest.raises(ValueError):
        masks.get_mask_card_number(card_number_too_long)


def test_get_mask_card_no_number(card_number_empty):
    with pytest.raises(TypeError):
        masks.get_mask_card_number(card_number_empty)


def test_get_mask_card_number_invalid(card_number_invalid):
    with pytest.raises(TypeError):
        masks.get_mask_card_number(card_number_invalid)


@pytest.mark.parametrize(
    "account, expected_mask",
    [
        ("123456789098765", "**8765"),
        ("9998887776665554443210", "**3210"),
        ("1223334444555556666667777777888888", "**8888"),
    ]
)
def test_get_mask_account(account, expected_mask):
    assert masks.get_mask_account(account) == expected_mask


def test_get_mask_account_too_short(account_too_short):
    with pytest.raises(ValueError):
        masks.get_mask_account(account_too_short)


def test_get_mask_account_too_long(account_too_long):
    with pytest.raises(ValueError):
        masks.get_mask_account(account_too_long)


def test_get_mask_account_empty(account_empty):
    with pytest.raises(TypeError):
        masks.get_mask_account(account_empty)


def test_get_mask_account_invalid(account_invalid):
    with pytest.raises(TypeError):
        masks.get_mask_account(account_invalid)

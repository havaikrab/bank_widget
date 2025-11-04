import pytest

from src import masks


@pytest.mark.parametrize('card_number, expected_mask', [(1234567890098765, '1234 56** **** 8765'),
                                                        (9988776543210, '9988 77** **** 3210'),
                                                        (1223334444555556666, '1223 33** **** 6666')])
def test_get_mask_card_number(card_number: int, expected_mask: str):
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


def test_get_mask_card_number_float(card_number_float):
    with pytest.raises(TypeError):
        masks.get_mask_card_number(card_number_float)

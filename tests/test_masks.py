import pytest

from src import masks


@pytest.mark.parametrize('some_card_number, expected_mask', [(1234567890098765, '1234 56** **** 8765'),
                                                             (9988776543210, '9988 77** **** 3210'),
                                                             (1223334444555556666, '1223 33** **** 6666')])

def test_get_mask_card_number(some_card_number: int, expected_mask: str):
    assert masks.get_mask_card_number(some_card_number) == expected_mask


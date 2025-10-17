def get_mask_card_number(card_number: int) -> str:
    """Возвращает маску намера карты"""

    first_slice = list(str(card_number)[:6])
    first_slice.insert(4, " ")
    first_str = "".join(first_slice)
    end_str = str(card_number)[-4:]
    masked_card_number = first_str + "** **** " + end_str
    return masked_card_number


def get_mask_account(account: int) -> str:
    """Возвращает маску намера счета"""

    end_str = str(account)[-4:]
    masked_account = "**" + end_str
    return masked_account

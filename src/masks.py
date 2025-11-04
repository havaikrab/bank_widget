def get_mask_card_number(card_number: int) -> str:
    """Возвращает маску намера карты"""

    if not isinstance(card_number, int):
        raise TypeError("Некорректный номер карты")
    if 12 < len(str(card_number)) < 20:
        first_slice = list(str(card_number)[:6])
        first_slice.insert(4, " ")
        first_str = "".join(first_slice)
        end_str = str(card_number)[-4:]
        masked_card_number = first_str + "** **** " + end_str
        return masked_card_number
    else:
        raise ValueError("Некорректный номер карты")


def get_mask_account(account: int) -> str:
    """Возвращает маску намера счета"""

    if not isinstance(account, int):
        raise TypeError("Некорректный номер счета")
    if 14 < len(str(account)) < 35:
        end_str = str(account)[-4:]
        masked_account = "**" + end_str
        return masked_account
    else:
        raise ValueError("Некорректный номер счета")

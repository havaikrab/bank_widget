from masks import get_mask_card_number, get_mask_account

def mask_account_card(requisites: str) -> str:
    """Возвращает маску номера счета или карты"""

    requisites_number = ''
    requisites_type = ''
    for i in requisites:
        if i.isdigit():
            requisites_number += i
        elif i.isalpha() or i == ' ':
            requisites_type += i
    if 'счет' in requisites_type.lower() or 'счёт' in requisites_type.lower():
        requisites_mask = 'Счет ' + get_mask_account(requisites_number)
    else:
        requisites_type = requisites_type.strip()
        requisites_mask = requisites_type + ' ' + get_mask_card_number(requisites_number)
    return requisites_mask


def get_date(detailed_log: str) -> str:
    """Возвращает дату лога"""
    data_list = detailed_log.split('-')
    day = data_list[2][:2]
    data_list[2] = day
    data = '.'.join(data_list[::-1])
    return data

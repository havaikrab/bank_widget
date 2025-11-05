from src import masks


def mask_account_card(requisites: str) -> str:
    """Возвращает маску номера счета или карты"""

    requisites_number = ""
    requisites_type = ""
    for i in requisites:
        if i.isdigit():
            requisites_number += i
        elif i.isalpha() or i == " ":
            requisites_type += i
    if "счет" in requisites_type.lower() or "счёт" in requisites_type.lower():
        requisites_mask = "Счет " + masks.get_mask_account(requisites_number)
    else:
        requisites_type = requisites_type.strip()
        if ' ' in requisites_type:
            requisites_type_list = []
            for i in requisites_type:
                if i.isalpha():
                    requisites_type_list.append(i)
                elif requisites_type_list[-1].isalpha():
                    requisites_type_list.append(i)
            requisites_type = ''.join(requisites_type_list)
        requisites_mask = requisites_type + " " + masks.get_mask_card_number(requisites_number)
    return str(requisites_mask)


def get_date(detailed_log: str) -> str:
    """Возвращает дату лога"""

    data_list = detailed_log.split("-")
    day = data_list[2][:2]
    data_list[2] = day
    data = ".".join(data_list[::-1])
    return data

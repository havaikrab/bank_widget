from src import masks


def mask_account_card(requisites: str) -> str:
    """Возвращает маску номера счета или карты"""

    if not isinstance(requisites, str):
        raise TypeError("Некорректный формат ввода реквизитов")

    requisites_number = ""
    requisites_type = ""
    requisites_type_no_spaces = ""

    for i in requisites:
        if i.isalpha() and len(requisites_number) == 0:
            requisites_type += i
            requisites_type_no_spaces += i
        elif i.isalpha() and len(requisites_number) != 0:
            raise ValueError("Некорректный формат ввода реквизитов")
        elif i.isdigit() and len(requisites_type_no_spaces) != 0:
            requisites_number += i
        elif i.isdigit() and len(requisites_type_no_spaces) == 0:
            raise ValueError("Некорректный формат ввода реквизитов")
        elif i == " ":
            requisites_type += i
        else:
            raise ValueError("Некорректный формат ввода реквизитов")

    if len(requisites_number) == 0 or len(requisites_type_no_spaces) == 0:
        raise ValueError("Некорректный формат ввода реквизитов")

    requisites_type = requisites_type.strip()
    if " " in requisites_type:
        requisites_type_list = []
        for i in requisites_type:
            if i.isalpha():
                requisites_type_list.append(i)
            elif requisites_type_list[-1].isalpha():
                requisites_type_list.append(i)
        requisites_type = "".join(requisites_type_list)

    if requisites_type.lower() == "счет" or requisites_type.lower() == "счёт":
        requisites_mask = "Счет " + masks.get_mask_account(requisites_number)
    else:
        requisites_mask = requisites_type + " " + masks.get_mask_card_number(requisites_number)
    return requisites_mask


def get_date(detailed_log: str) -> str:
    """Возвращает строку 'год.месяц.день' из строки 'год-месяц-деньTчасы:минуты:секунды'"""

    if not isinstance(detailed_log, str):
        raise TypeError("Некорректный формат даты")
    if len(detailed_log) == 0:
        raise ValueError("Некорректный формат даты")

    symbol_index_dict = {4: "-", 7: "-", 10: "T", 13: ":", 16: ":"}
    for i in range(19):
        if not detailed_log[i].isdigit():
            if detailed_log[i] != symbol_index_dict.get(i):
                print('"Некорректный формат даты"')
                return ""

    date_list = detailed_log.split("-")
    day = date_list[2][:2]
    date_list[2] = day
    date = ".".join(date_list[::-1])
    return date

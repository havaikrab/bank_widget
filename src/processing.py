from typing import Dict, List


def filter_by_state(dicts_list: list[dict], state: str = "EXECUTED") -> list:
    """Возвращает список словарей с указанным значением state из передаваемого списка словарей,
    по умолчанию state = 'EXECUTED'"""

    if not isinstance(dicts_list, List):
        raise TypeError("Некорректный формат данных")
    for d in dicts_list:
        if not isinstance(d, Dict):
            raise ValueError("Некорректный формат данных")

    filtered_list = []
    for d in dicts_list:
        if d.get("state") == state:
            filtered_list.append(d)
    return filtered_list


def sort_by_date(dicts_list: list, sort_reverse: bool = True) -> list:
    """Возвращает передаваемый список словарей, отсортированным по дате,
    по умолчанию в обратном хронологическом порядке"""

    if not isinstance(dicts_list, List):
        raise TypeError("Некорректный формат данных")

    for d in dicts_list:
        if not isinstance(d, Dict):
            raise ValueError("Некорректный формат данных")

        symbol_index_dict = {4: "-", 7: "-", 10: "T", 13: ":", 16: ":"}
        for i in range(19):
            if not d["date"][i].isdigit():
                if d.get("date", "")[i] != symbol_index_dict.get(i):
                    print("Транзакция имеет некорректный формат даты")
                    break

    sorted_list = sorted(dicts_list, key=lambda dictionary: dictionary["date"], reverse=sort_reverse)
    return sorted_list

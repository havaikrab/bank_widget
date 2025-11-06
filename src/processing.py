from typing import List, Dict

def filter_by_state(dicts_list: list[dict], state: str = "EXECUTED") -> list:
    """Возвращает список словарей с указанным значением state из передаваемого списка словарей,
    по умолчанию state = 'EXECUTED'"""

    if not isinstance(dicts_list, List):
        raise TypeError("Некорректный формат данных")
    for d in dicts_list:
        if not isinstance(d, Dict):
            raise ValueError("Некорректный формат данных")
        elif 'id' not in d or 'state' not in d or 'date' not in d:
            raise ValueError("Некорректный формат данных")

    filtered_list = []
    for dict in dicts_list:
        if dict.get("state") == state:
            filtered_list.append(dict)
    return filtered_list


def sort_by_date(dicts_list: list, sort_reverse: bool = True) -> list:
    """Возвращает передаваемый список словарей, отсортированным по дате,
    по умолчанию в обратном хронологическом порядке"""

    sorted_list = sorted(dicts_list, key=lambda dict: dict["date"], reverse=sort_reverse)
    return sorted_list

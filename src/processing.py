from typing import List, Dict

from src.widget import get_date

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

    if not isinstance(dicts_list, List):
        raise TypeError("Некорректный формат данных")

    for d in dicts_list:
        if not isinstance(d, Dict):
            raise ValueError("Некорректный формат данных")
        elif 'id' not in d or 'state' not in d or 'date' not in d or len(d['date']) < 21:
            raise ValueError("Некорректный формат данных")

        symbol_index_dict = {4: '-', 7: '-', 10: 'T', 13: ':', 16: ':', 19: '.'}
        for i in range(len(d['date'])):
            if not d['date'][i].isdigit():
                if d['date'][i] != symbol_index_dict[i]:
                    raise KeyError("Некорректный формат данных")

    sorted_list = sorted(dicts_list, key=lambda dictionary: dictionary["date"], reverse=sort_reverse)
    return sorted_list

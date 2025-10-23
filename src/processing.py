def filter_by_state(dicts_list: list, state="EXECUTED") -> list:
    '''Возвращает список словарей с указанным значением state из передаваемого списка словарей,
    по умолчанию state = "EXECUTED"'''
    filtred_list = []
    for dict in dicts_list:
        if dict.get("state") == state:
            filtred_list.append(dict)
    return filtred_list


def sort_by_date(dicts_list: list, sort_reverse=True) -> list:
    '''Возвращает передаваемый список словарей, отсортированным по дате,
    по умолчанию в обратном хронологическом порядке'''
    sorted_list = sorted(dicts_list, key=lambda dict: dict['date'], reverse=sort_reverse)
    return sorted_list




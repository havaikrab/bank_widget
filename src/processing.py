def filter_by_state(dicts_list: list, state="EXECUTED") -> list:
    '''Возвращает список словарей с указанным значением state из заданного списка словарей,
    по умолчанию state = "EXECUTED"'''
    filtred_list = []
    for dict in dicts_list:
        if dict.get("state") == state:
            filtred_list.append(dict)
    return filtred_list


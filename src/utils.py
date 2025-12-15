from typing import List, Dict
import json


def get_transactions(path_to_file: str) -> List[Dict]:
    '''Возвращает список словарей-транзакций из указанного файла'''

    try:
        with open(path_to_file, 'r', encoding='utf-8') as data:
            transactions_list = json.load(data)
            if type(transactions_list) != list:
                return []
            else:
                return transactions_list
    except Exception:
        return []
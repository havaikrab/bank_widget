import re

def find_description(transactions_list: list, text: str) -> list:
    """Возвращает список словарей-транзакций по заданному описанию"""

    pattern = re.compile(r'\b\w+\b')
    key_words = re.findall(pattern, text)
    required_list = []
    for transaction in transactions_list:
        for word in key_words:
            if word.lower() in transaction.get('description', '').lower():
                required_list.append(transaction)
                break
    return required_list

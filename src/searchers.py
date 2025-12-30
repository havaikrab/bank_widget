import re
from collections import Counter


def find_description(transactions_list: list, text: str) -> list:
    """Возвращает список словарей-транзакций, в описании которых есть слова из передаваемой строки"""

    pattern = re.compile(r"\b\w+\b")
    key_words = re.findall(pattern, text)
    key_words_roots = [word[:-2] for word in key_words if len(word) > 2]
    required_list = []
    for transaction in transactions_list:
        for word in key_words_roots:
            if word.lower() in transaction.get("description", "").lower():
                required_list.append(transaction)
                break
    return required_list


def aggregate_by_description(transactions_list: list, requirements_list: list):
    """Возвращает словарь, содержащий названия категорий транзакций
    с количеством вхождений соответствующей категории в список словарей-транзакций"""

    descriptions = (
        transaction.get("description")
        for transaction in transactions_list
        if transaction.get("description") in requirements_list
    )
    counted_descriptions = Counter(descriptions)
    return dict(counted_descriptions)

from typing import Iterator, List


def filter_by_currency(transactions: List[dict], currency_code: str) -> Iterator:
    """Возвращает итератор со словарями-транзакциями с указанной валютой"""

    if not isinstance(transactions, List):
        raise TypeError("Некорректный формат данных")

    for transaction in transactions:
        if (
            isinstance(transaction, dict)
            and "operationAmount" in transaction
            and "currency" in transaction["operationAmount"]
            and "code" in transaction["operationAmount"]["currency"]
            and transaction["operationAmount"]["currency"]["code"] == currency_code
        ):
            yield transaction


def transaction_descriptions(transactions: List[dict]) -> Iterator:
    """Возвращает итератор с описанием транзакций"""

    if not isinstance(transactions, List):
        raise TypeError("Некорректный формат данных")

    for transaction in transactions:
        if isinstance(transaction, dict) and "description" in transaction:
            yield transaction["description"]

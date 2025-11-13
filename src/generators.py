from typing import Iterator, List


def filter_by_currency(transactions: List[dict], currency_code: str) -> Iterator:
    """Возвращает спсок словарей-транзакций с указанной валютой"""


    filtered_transactions = (transaction for transaction in transactions
                             if isinstance(transaction, dict)
                             and "operationAmount" in transaction
                             and "currency" in transaction["operationAmount"]
                             and "code" in transaction["operationAmount"]["currency"]
                             and transaction["operationAmount"]["currency"]["code"] == currency_code)

    for transaction in filtered_transactions:
        yield transaction

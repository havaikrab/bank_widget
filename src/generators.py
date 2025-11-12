def filter_by_currency(transactions: list, currency: str) -> list:
    """Возвращает спсок словарей-транзакций с указанной валютой"""

    if not isinstance(transactions, list):
        raise TypeError("Некорректный формат источника данных")

    filtered_transactions = (transaction for transaction in transactions if
                             transaction["operationAmount"]["currency"]["name"] == currency)

    for transaction in filtered_transactions:
        yield transaction
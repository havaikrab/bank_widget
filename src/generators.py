def filter_by_currency(transactions: list, currency_code: str) -> dict:
    """Возвращает спсок словарей-транзакций с указанной валютой"""

    if not isinstance(transactions, list):
        raise TypeError("Некорректный формат источника данных")

    filtered_transactions = (transaction for transaction in transactions if
                             transaction["operationAmount"]["currency"]["code"] == currency_code)

    for transaction in filtered_transactions:
        yield transaction
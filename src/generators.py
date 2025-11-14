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


def card_number_generator(start: int, stop: int) -> str:
    '''Возвращает итератор с номерами карт в указанном диапазоне'''

    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("Некорректный формат введенного диапазона")
    if start < 1 or stop > int('9' * 16) or start > stop:
        raise ValueError("Некорректный формат введенного диапазона")

    for num in range(start, (stop + 1)):
        num_str = str(num)
        while len(num_str) < 16:
            num_str = '0' + num_str
        card_number = num_str[:4] + ' ' + num_str[4:8] + ' ' + num_str[8:12] + ' ' + num_str[12:]
        yield card_number

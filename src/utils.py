import json
from typing import Dict, List

from src import external_api


def get_transactions(path_to_file: str) -> List[Dict]:
    """Возвращает список словарей-транзакций из указанного файла"""

    try:
        with open(path_to_file, "r", encoding="utf-8") as data:
            transactions_list = json.load(data)
            if not isinstance(transactions_list, list):
                return []
            else:
                return transactions_list
    except Exception:
        return []


def get_amount_rubles(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублевом эквиваленте"""

    if (
        isinstance(transaction, dict)
        and "date" in transaction
        and "operationAmount" in transaction
        and "amount" in transaction["operationAmount"]
        and "currency" in transaction["operationAmount"]
        and "code" in transaction["operationAmount"]["currency"]
    ):

        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            return float(transaction["operationAmount"]["amount"])

        else:
            symbol_index_dict = {4: "-", 7: "-", 10: "T", 13: ":", 16: ":", 19: "."}
            for i in range(len(transaction["date"])):
                if not transaction["date"][i].isdigit():
                    if transaction["date"][i] != symbol_index_dict[i]:
                        raise KeyError("Некорректный формат данных")

            transaction_date = transaction["date"][:10]
            currency_rate = external_api.get_currency_rate_by_date(
                transaction["operationAmount"]["currency"]["code"], transaction_date
            )
            if currency_rate["status"]:
                if currency_rate["rate"] is not None:
                    amount_rubles = round((float(transaction["operationAmount"]["amount"]) / currency_rate["rate"]), 2)
                    return amount_rubles
                else:
                    print("Неизвестный код валюты транзакции")
                    return 0.0
            else:
                return 0.0
    else:
        raise ValueError("Некорректный формат данных")

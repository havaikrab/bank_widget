import json
import logging
import os
from typing import Dict, List

from src import external_api


utils_logger = logging.getLogger("utils_logger")
os.makedirs("logs/", exist_ok=True)
file_handler = logging.FileHandler("logs/utils_logs.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def get_transactions(path_to_file: str) -> List[Dict]:
    """Возвращает список словарей-транзакций из указанного файла"""

    utils_logger.info("Вызвана функция get_transactions")
    try:
        with open(path_to_file, "r", encoding="utf-8") as data:
            transactions_list = json.load(data)
            if not isinstance(transactions_list, list):
                utils_logger.warning("Содержимое открываемого файла не соответствует ожидаемому формату")
                return []
            else:
                utils_logger.info("Содержимое открываемого файла успешно преобразовано в объект Python")
                return transactions_list
    except Exception as exc:
        utils_logger.error(f"При вызове функции произошла ошибка {exc}")
        return []


def get_amount_rubles(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублевом эквиваленте"""

    utils_logger.info("Вызвана функция get_amount_rubles")
    if (
        isinstance(transaction, dict)
        and "date" in transaction
        and "operationAmount" in transaction
        and "amount" in transaction["operationAmount"]
        and "currency" in transaction["operationAmount"]
        and "code" in transaction["operationAmount"]["currency"]
    ):

        utils_logger.info("Аргумент передаваемый функции соответствует ожидаемому формату данных")
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            utils_logger.info("Сумма транзакции успешно получена без применения конвертации валют")
            return float(transaction["operationAmount"]["amount"])

        else:
            symbol_index_dict = {4: "-", 7: "-", 10: "T", 13: ":", 16: ":", 19: "."}
            for i in range(len(transaction["date"])):
                if not transaction["date"][i].isdigit():
                    if transaction["date"][i] != symbol_index_dict[i]:
                        utils_logger.error("Дата транзакции имеет некорректный формат, работа завршена с ошибкой")
                        raise KeyError("Некорректный формат данных")

            transaction_date = transaction["date"][:10]
            currency_rate = external_api.get_currency_rate_by_date(
                transaction["operationAmount"]["currency"]["code"], transaction_date
            )
            utils_logger.info("Попытка получения сведений о курсе валюты транзакции из внешнего источника")
            if currency_rate["status"]:
                utils_logger.info("Запрос успешно отправлен")
                if currency_rate["rate"] is not None:
                    amount_rubles = round((float(transaction["operationAmount"]["amount"]) / currency_rate["rate"]), 2)
                    utils_logger.info("Сумма транзакции успешно получена с применением конвертации валют")
                    return amount_rubles
                else:
                    print("Неизвестный код валюты транзакции")
                    utils_logger.warning("Неизвестный код валюты транзакции")
                    return 0.0
            else:
                utils_logger.warning("Неудачная поптка обращения к внешнему ресурсу")
                return 0.0
    else:
        utils_logger.error("Некорректный формат данных, работа завершена с ошибкой")
        raise ValueError("Некорректный формат данных")

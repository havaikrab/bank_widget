from src import utils, data_readers, processing, searchers, widget
from collections import Counter


def get_output_form(transaction: dict) -> dict:
    result_dict = dict()
    if transaction.get("operationAmount").get("amount"):
        result_dict["head"] = str(widget.get_date(transaction.get("date"))) + " " + transaction.get("description")
        sender = ""
        if transaction.get("from"):
            sender = str(widget.mask_account_card(transaction.get("from"))) + " -> "
        result_dict["from_to"] = sender + str(widget.mask_account_card(transaction.get("to")))
        result_dict["amount"] = (
            "Сумма: "
            + str(transaction.get("operationAmount").get("amount"))
            + " "
            + str(transaction.get("operationAmount").get("currency").get("name"))
        )
    return result_dict


data_source = {
    "1": ["JSON", "data/operations.json", utils.get_transactions],
    "2": ["CSV", "data/transactions.csv", data_readers.csv_data_reader],
    "3": ["XLSX", "data/transactions_excel.xlsx", data_readers.xlsx_data_reader],
}

if __name__ == "__main__":
    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями.                                                                                     
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла.
    2. Получить информацию о транзакциях из CSV-файла.
    3. Получить информацию о транзакциях из XLSX-файла."""
    )

    called_data = input()
    while called_data not in data_source:
        print("Для продолжения введите число 1, 2 или 3")
        called_data = input()

    print(f"В качестве источника данных выбран {data_source[called_data][0]}-файл.")
    transactions = data_source[called_data][2](data_source[called_data][1])

    print(
        """Введите статус операций, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: PENDING, CANCELED, EXECUTED"""
    )
    while True:
        called_state = input().upper()
        if called_state == "PENDING" or called_state == "CANCELED" or called_state == "EXECUTED":
            break
        print("Пожалуйста, введите один из предложенных вариантов статуса операций: PENDING, CANCELED, EXECUTED")
    filtered_by_state_data = processing.filter_by_state(transactions, state=called_state)

    print("Отсортировать операции по дате? Да / Нет")
    while True:
        sort_by_date = input().lower()
        if sort_by_date == "да":
            print(
                """Укажите, в каком порядке нужно отсортировать операции?
По возрастанию / По убыванию
По возрастанию - от старых операций к новым.
По убыванию - от новых операций к старым."""
            )

            while True:
                sort_direction = input().lower()
                if "возрастан" in sort_direction and "убыван" not in sort_direction:
                    date_reverse = False
                    break

                elif "убыван" in sort_direction and "возрастан" not in sort_direction:
                    date_reverse = True
                    break

                print("Извините, ваш ответ не ясен, пожалуйста, введите: ПО ВОЗРАСТАНИЮ или ПО УБЫВАНИЮ")
            sorted_by_date_data = processing.sort_by_date(filtered_by_state_data, sort_reverse=date_reverse)
            break

        elif sort_by_date == "нет":
            sorted_by_date_data = filtered_by_state_data
            break

        print("Извините, ваш ответ не ясен, пожалуйста, введите: ДА или НЕТ")

    print("Желаете ли вы увидеть только рублевые операции? Да / Нет")
    while True:
        rubles_transactions = input().lower()
        if rubles_transactions == "нет":
            sorted_by_currency_data = sorted_by_date_data
            break

        elif rubles_transactions == "да":
            sorted_by_currency_data = [
                transaction
                for transaction in sorted_by_date_data
                if transaction.get("operationAmount").get("currency").get("code") == "RUB"
            ]
            break

        print("Извините, ваш ответ не ясен, пожалуйста, введите: ДА или НЕТ")

    print("Желаете ли вы отфильтровать операции по определенному слову в описании? Да / Нет")
    counted_descriptions = None
    while True:
        key_words_filter = input().lower()
        if key_words_filter == "нет":
            sorted_by_description_data = sorted_by_currency_data
            result_data = [get_output_form(transaction) for transaction in sorted_by_description_data]
            break

        elif key_words_filter == "да":
            print("Пожалуйста, введите ключевые слова для поиска соответствующих операций")
            key_words = input()
            sorted_by_description_data = searchers.find_description(sorted_by_currency_data, key_words)
            result_data = [get_output_form(transaction) for transaction in sorted_by_description_data]
            descriptions_list = [transaction.get("description") for transaction in sorted_by_description_data]
            counted_descriptions = dict(Counter(descriptions_list))
            break

        print("Извините, ваш ответ не ясен, пожалуйста, введите: ДА или НЕТ")

    result_count = len(result_data)
    if result_count == 0:
        print("Операций, подходящих под описание не найдено")
    else:
        print("Пожалуйста, вот список интересующих вас операций")
        print(f"Всего операций {result_count}")
        if counted_descriptions:
            for k, v in counted_descriptions.items():
                print(f"{k}: {v}")
        for transaction in result_data:
            print("")
            for v in transaction.values():
                print(v)

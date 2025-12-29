from src import utils, data_readers, processing
import json

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
        if called_state == 'PENDING' or called_state == 'CANCELED' or called_state == 'EXECUTED':
            break
        print("Пожалуйста, введите один из предложенных вариантов статуса операций: PENDING, CANCELED, EXECUTED")
    filtered_by_state_data = processing.filter_by_state(transactions, state=called_state)

    print('Отсортировать операции по дате? Да / Нет')
    while True:
        sort_by_date = input().lower()
        if sort_by_date == 'да':
            print('''Укажите, в каком порядке нужно отсортировать операции?
По возрастанию / По убыванию
По возрастанию - от старых операций к новым.
По убыванию - от новых операций к старым.''')

            while True:
                sort_direction = input().lower()
                if 'возрастан' in sort_direction and 'убыван' not in sort_direction:
                    date_reverse = False
                    break

                elif 'убыван' in sort_direction and 'возрастан' not in sort_direction:
                    date_reverse = True
                    break

                print('Извините, ваш ответ не ясен, пожалуйста, введите: ПО ВОЗРАСТАНИЮ или ПО УБЫВАНИЮ')
            sorted_by_date_data = processing.sort_by_date(filtered_by_state_data, sort_reverse=date_reverse)
            break

        elif sort_by_date == 'нет':
            sorted_by_date_data = filtered_by_state_data
            break

        print('Извините, ваш ответ не ясен, пожалуйста, введите: ДА или НЕТ')

    print('Желаете ли вы увидеть только рублевые операции? Да / Нет')
    while True:
        rubles_transactions = input().lower()
        if rubles_transactions == 'нет':
            print('''Для операций с валютой, отличной от рубля,
необходима ли информация о сумме транзакций в рублевом эквиваленте на момент совершения операции? Да / Нет''')
            while True:
                convertion = input().lower()
                if convertion == 'нет':
                    sorted_by_currency_data = sorted_by_date_data
                    break

                elif convertion == 'да':
                    sorted_by_currency_data = []
                    for transaction in sorted_by_date_data:
                        if transaction.get('operationAmount').get('currency').get('code') != 'RUB':
                            transaction.get('operationAmount')['convertedToRublesAmount'] = utils.get_amount_rubles(transaction)
                            sorted_by_currency_data.append(transaction)
                        else:
                            sorted_by_currency_data.append(transaction)
                    break

                print('Извините, ваш ответ не ясен, пожалуйста, введите: ДА или НЕТ')


        elif rubles_transactions == 'да':
            sorted_by_currency_data = [transaction for transaction in sorted_by_date_data if transaction.get('operationAmount').get('currency').get('code') == 'RUB']
            break

        print('Извините, ваш ответ не ясен, пожалуйста, введите: ДА или НЕТ')










    print(json.dumps(sorted_by_currency_data, indent=4, ensure_ascii=False))
    print(len(sorted_by_currency_data))

# json - pending - 0
# csv - pending - 146  9
# xl - pending - 146   9

# json - cancel - 15   9
# csv - cancel - 158   11
# xl - cancel - 158    11


# json - executed - 85 40
# csv - executed - 695 34
# xl - executed - 695

import pandas as pd
import logging
import os


data_readers_logger = logging.getLogger("data_readers_logger")
os.makedirs("logs/", exist_ok=True)
file_handler = logging.FileHandler("logs/data_readers_logger.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
data_readers_logger.addHandler(file_handler)
data_readers_logger.setLevel(logging.DEBUG)


def csv_data_reader(path_to_file: str) -> list:
    '''Возвращает список отформатированных словарей-транзакций из передаваемого csv-файла'''

    data_readers_logger.info("Вызвана функция csv_data_reader")
    try:
        data_readers_logger.info(f"Попытка открыть файл базы данных {path_to_file}")
        with open(path_to_file, 'r', encoding='utf-8') as file:
            head = file.read().split('\n')[0]
            if head == '':
                data_readers_logger.warning('Файл базы данных был успешно открыт, но является пустым')
                return []
            symbols = {}
            for i in head:
                if not i.isalpha() and not i.isdigit() and i != ' ':
                    symbols[i] = 0
            delimiter_count = 0
            delimiter = ','
            for k in symbols.keys():
                symbols[k] = head.count(k)
                if symbols[k] >= delimiter_count:
                    delimiter_count = symbols[k]
                    delimiter = k
            data_readers_logger.info('Файл базы данных был успешно открыт')
            data_readers_logger.info(f'В качестве разделителя принят символ "{delimiter}"')
    except FileNotFoundError:
        data_readers_logger.error(f"Файл {path_to_file} не найден")
        return []
    else:
        reader = pd.read_csv(path_to_file, delimiter=delimiter)
        reader.columns = reader.columns.str.lower()
        expected_columns = {'id': False, 'state': False, 'date': False, 'amount': False, 'currency_name': False, 'currency_code': False, 'description': False, 'from': False, 'to': False}
        for k in expected_columns.keys():
            if k in reader:
                expected_columns[k] = True
        if not all(expected_columns.values()):
            data_readers_logger.warning('Файл базы данных содержит не все ожидаемые названия заголовков')
        currency_available_columns = []
        currency_columns = []
        if expected_columns['currency_name']:
            currency_available_columns.append('currency_name')
            currency_columns.append('name')
        if expected_columns['currency_code']:
            currency_available_columns.append('currency_code')
            currency_columns.append('code')
        if currency_available_columns:
            currency = reader.loc[:, currency_available_columns]
            currency.columns = currency_columns
            currency_list = currency.to_dict(orient='records')
            reader = reader.assign(currency=currency_list)
        amount_available_columns = []
        if expected_columns['amount']:
            amount_available_columns.append('amount')
        if 'currency' in reader:
            amount_available_columns.append('currency')
        if amount_available_columns:
            operation_amount = reader.loc[:, amount_available_columns]
            operation_amount_list = operation_amount.to_dict(orient='records')
            reader = reader.assign(operationAmount=operation_amount_list)
        required_columns = ['id', 'state', 'date', 'operationAmount', 'description', 'from', 'to']
        available_columns = []
        for i in required_columns:
            if i in reader:
                available_columns.append(i)
        sorted_reader = []
        if available_columns:
            sorted_reader = reader.loc[:, available_columns]
            sorted_reader = sorted_reader.to_dict(orient='records')
            data_readers_logger.info(f'Сформирована база данных с заголовками "{available_columns}"')
        else:
            data_readers_logger.warning(f'Файл {path_to_file} не содержит ожидаемых данных')
        return sorted_reader



def xlsx_data_reader(path_to_file: str) -> list:
    '''Возвращает список отформатированных словарей-транзакций из передаваемого xlsx-файла'''

    data_readers_logger.info("Вызвана функция xlsx_data_reader")
    try:
        data_readers_logger.info(f"Попытка открыть файл базы данных {path_to_file}")
        reader = pd.read_excel(path_to_file)
        if reader.empty:
            data_readers_logger.warning('Файл базы данных был успешно открыт, но является пустым')
            return []
    except FileNotFoundError:
        data_readers_logger.error(f"Файл {path_to_file} не найден")
        return []
    else:
        reader.columns = reader.columns.str.lower()
        expected_columns = {'id': False, 'state': False, 'date': False, 'amount': False, 'currency_name': False,
                            'currency_code': False, 'description': False, 'from': False, 'to': False}
        for k in expected_columns.keys():
            if k in reader:
                expected_columns[k] = True
        if not all(expected_columns.values()):
            data_readers_logger.warning('Файл базы данных содержит не все ожидаемые названия заголовков')
        currency_available_columns = []
        currency_columns = []
        if expected_columns['currency_name']:
            currency_available_columns.append('currency_name')
            currency_columns.append('name')
        if expected_columns['currency_code']:
            currency_available_columns.append('currency_code')
            currency_columns.append('code')
        if currency_available_columns:
            currency = reader.loc[:, currency_available_columns]
            currency.columns = currency_columns
            currency_list = currency.to_dict(orient='records')
            reader = reader.assign(currency=currency_list)
        amount_available_columns = []
        if expected_columns['amount']:
            amount_available_columns.append('amount')
        if 'currency' in reader:
            amount_available_columns.append('currency')
        if amount_available_columns:
            operation_amount = reader.loc[:, amount_available_columns]
            operation_amount_list = operation_amount.to_dict(orient='records')
            reader = reader.assign(operationAmount=operation_amount_list)
        required_columns = ['id', 'state', 'date', 'operationAmount', 'description', 'from', 'to']
        available_columns = []
        for i in required_columns:
            if i in reader:
                available_columns.append(i)
        sorted_reader = []
        if available_columns:
            sorted_reader = reader.loc[:, available_columns]
            sorted_reader = sorted_reader.to_dict(orient='records')
            data_readers_logger.info(f'Сформирована база данных с заголовками "{available_columns}"')
        else:
            data_readers_logger.warning(f'Файл {path_to_file} не содержит ожидаемых данных')
        return sorted_reader

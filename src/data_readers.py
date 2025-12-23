import pandas as pd

def csv_data_reader(path_to_file: str) -> list:
    '''Возвращает список отформатированных словарей-транзакций из передаваемого csv-файла'''

    reader = pd.read_csv(path_to_file, delimiter=';')

    currency = reader.loc[:, ['currency_name', 'currency_code']]
    currency.columns = ['name', 'code']
    currency_list = currency.to_dict(orient='records')
    reader = reader.assign(currency=currency_list)

    operation_amount = reader.loc[:, ['amount', 'currency']]
    operation_amount_list = operation_amount.to_dict(orient='records')
    reader = reader.assign(operationAmount=operation_amount_list)

    sorted_reader = reader.loc[:, ['id', 'state', 'date', 'operationAmount', 'description', 'from', 'to']]

    return sorted_reader.to_dict(orient='records')


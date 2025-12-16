import os

import requests
from dotenv import load_dotenv


def get_currency_rate_by_date(currency_code: str, date: str) -> dict:
    """Возвращает курс заданной валюты по отношению к рублю в указанную дату"""
    url = f"https://api.apilayer.com/currency_data/historical?date={date}&source=RUB"
    load_dotenv()
    api_key = os.getenv("exchangerates_API_KEY")
    headers = {"apikey": api_key}
    try:
        response = requests.get(url, headers=headers)
        status_code = response.status_code
        if status_code == 200:
            conversion_status = True
            rate_data = response.json()
            currency_rate = rate_data["quotes"].get(f"RUB{currency_code}")
        else:
            print("Для обращения к внешней базы данных необходима аутентификация пользователя")
            conversion_status = False
            currency_rate = None
    except Exception:
        print("Нестабильное подключение к сети или внешняя база данных временно недоступна")
        conversion_status = False
        currency_rate = None
    finally:
        return {"status": conversion_status, "rate": currency_rate}

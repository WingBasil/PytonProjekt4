import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


def convert_from_usd_to_rub(amount:float) -> Any:
    """Функция принимает значение в долларах, обращается к API и возвращает конвертацию в рубли"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount}"
    headers = {"apikey": api_key}
    response = requests.request("GET", url, headers=headers)
    json_result = response.text
    rub_amount = json.loads(json_result)["result"]

    return rub_amount


def convert_from_eur_to_rub(amount: float) -> Any:
    """Функция принимает значение в евро, обращается к API и возвращает конвертацию в рубли"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={amount}"
    headers = {"apikey": api_key}
    response = requests.request("GET", url, headers=headers)
    json_result = response.text
    rub_amount = json.loads(json_result)["result"]

    return rub_amount
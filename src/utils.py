import json
from typing import Any

from src.external_api import convert_to_rub

def get_transactions_dictionary(path: str) -> Any:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as operations:
            try:
                transactions_data = json.load(operations)
                print(transactions_data)
                return transactions_data
            except json.JSONDecodeError:
                transactions_data = []
                return transactions_data
    except FileNotFoundError:
        transactions_data = []
        return transactions_data


def transaction_amount_in_rub(transactions: list, transaction_id: int) -> Any:
    """Функция принимает ID транзакции и возвращает сумму транзакции в рублях,
    если сумма не в рублях, конвертирует в рубли"""
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                return transaction["operationAmount"]["amount"]
            elif transaction["operationAmount"]["currency"]["code"] == "USD":
                not_rub_amount = transaction["operationAmount"]["amount"]
                currency = transaction["operationAmount"]["currency"]["code"]
                rub_amount = round(convert_to_rub(not_rub_amount, currency), 2)
                return rub_amount
            elif transaction["operationAmount"]["currency"]["code"] == "EUR":
                currency = "EUR"
                not_rub_amount = transaction["operationAmount"]["amount"]
                rub_amount = round(convert_to_rub(not_rub_amount, currency), 2)
                return rub_amount

if __name__ == "__main__":
#get_transactions_dictionary("../data/operations.json")
    transactions = get_transactions_dictionary("../data/operations.json")
    print(transaction_amount_in_rub(transactions, 939719570))

from typing import Any
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_number: str) -> Any:
    """Анализирует принятую строку на наличие информации о счете или карте
    Формирует строку с Типом карты/Счетом + маска."""
    if "Счет" in input_number:
        account_number = int(input_number[-20:])
        new_text = "Счет " + get_mask_account(account_number)
    else:
        card_number = int(input_number[-16:])
        new_text = input_number[:-16] + get_mask_card_number(card_number)
    return new_text


def get_data(date: str) -> Any:
    """Функция преобразования даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


# print(get_data('2018-07-11T02:26:18.671407'))
input_number = "MasterCard 7158300734726758"
# input_number = "Счет 12345678901234567890"
print(mask_account_card(input_number))

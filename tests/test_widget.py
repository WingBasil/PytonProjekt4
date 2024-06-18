import pytest
from src.widget import mask_account_card, get_data


@pytest.fixture
def input_number():
    return "MasterCard 7158300734726758"

#@pytest.fixture
#def account_number():
#    return "Счет 12345678901234567890"

def test_mask_account_card(input_number):
    assert mask_account_card(input_number) == "MasterCard 71587158 30** **** 6758"

@pytest.fixture
def date():
    return "2018-07-11T02:26:18.671407"
def test_get_data(date):
    assert get_data(date) == "11.07.2018"
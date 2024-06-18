import pytest
from src.widget import get_mask_card_number
from src.masks import get_mask_card_number


@pytest.fixture
def input_number():
    return "MasterCard 7158300734726758"

#@pytest.fixture
#def account_number():
#    return "Счет 12345678901234567890"

def test_mask_account_card(input_number):
    assert mask_account_card(input_number) == "MasterCard 71587158 30** **** 6758"
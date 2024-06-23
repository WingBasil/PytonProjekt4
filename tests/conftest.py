import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator, transactions

@pytest.fixture
def test_transactions_1():
    return transactions
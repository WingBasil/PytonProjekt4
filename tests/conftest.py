import pytest
from src.processing import filter_by_state, sort_by_date, initial_list
from src.generators import transactions

@pytest.fixture
def test_transactions():
    return transactions

@pytest.fixture
def test_initial_list():
    return 'EXECUTED'

@pytest.fixture
def test_initial_list_1():
    return initial_list

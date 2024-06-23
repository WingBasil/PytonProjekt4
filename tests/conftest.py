import pytest

from src.generators import transactions


@pytest.fixture
def test_transactions():
    return transactions
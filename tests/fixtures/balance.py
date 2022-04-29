import pytest
from balance.models import BalanceEntry, Balance


@pytest.fixture
def balance():
    return Balance.objects.create(user_id=1, ticker_id=1, amount=19, hash="hash")


@pytest.fixture
def balance_user_two():
    return Balance.objects.create(user_id=2, ticker_id=1, amount=10, hash="hash")


@pytest.fixture
def transaction(balance):
    return BalanceEntry.objects.create(
        user_id=1, amount=10, amount_after=19, amount_before=12, balance=balance
    )

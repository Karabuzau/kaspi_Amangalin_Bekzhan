import pytest
from account.account import Account, CurrencyMismatchError
from uuid import uuid4
from decimal import Decimal
import json

class TestAccount:
    def test_account_create(self) -> None:
        account_id = uuid4()
        account = Account(
            id_=uuid4(),
            currency="KZT",
            balance=Decimal(10),
        )

        assert isinstance(account, Account)
        assert account.balance == 10

        account2 = Account(
            id_=uuid4(),
            currency="KZT",
            balance=Decimal(5),
        )
        assert account2 < account

    def test_errors(self) -> None:
        account = Account(
            id_=uuid4(),
            currency="KZT",
            balance=Decimal(10)
        )

        account2 = Account(
            id_=uuid4(),
            currency="USD",
            balance=Decimal(5)
        )
        with pytest.raises(CurrencyMismatchError):
            assert account2 < account
    def test_json_import_export(self)->None:
        account_id=uuid4()
        account=Account(
            id_=uuid4(),
            currency="KZT",
            balance=Decimal(10),
        )

        json_account = account.to_json()
        assert json.loads(json_account) == {"id": str(account.id_), "currency": account.currency, "balance": account.balance,}

from dataclasses import dataclass
from uuid import UUID
from decimal import Decimal
import json

class CurrencyMismatchError(ValueError):
    pass


@dataclass
class Account:
    id_: UUID
    currency: str
    balance: Decimal


    def __lt__(self, other):
        assert isinstance(other, Account)
        if self.currency != other.currency:
            raise CurrencyMismatchError
        return self.balance < other.balance

    def to_json(self) -> str:
        json_repr = {
            "id": str(self.id_),
            "currency": self.currency,
            "balance":float(self.balance)
        }
        return json.dumps(json_repr)
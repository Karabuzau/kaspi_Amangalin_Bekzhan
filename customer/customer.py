from dataclasses import dataclass
from uuid import UUID
from account.account import Account


@dataclass
class Customer:
    id_: UUID
    age: int
    first_name: str
    last_name: str
    accounts: list[Account]


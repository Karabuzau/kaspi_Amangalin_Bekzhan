from decimal import Decimal

import pytest

from account.account import Account
from customer.customer import Customer
from uuid import uuid4


class TestCustomer:
    def test_two_plus_two(self) ->None:
        assert 2+2==4

    def test_customer_create(self)->None:
        customer_id_=uuid4()
        customer=Customer(
            id_=customer_id_,
            age=23,
            first_name="Bekzhan",
            last_name="Amangalin",
            accounts=[]
        )

        assert customer.id_==customer_id_
        assert customer.first_name=="Bekzhan"
        assert customer.last_name=="Amangalin"


        customer2 = Customer(
            id_=customer_id_,
            age=23,
            first_name="Bekzhan",
            last_name="Amangalin",
            accounts=[]
        )

        assert isinstance(customer, Customer)
        assert customer==customer2


    def customer_create_with_accounts(self) ->None:
        account1_id=uuid4()
        account2_id=uuid4()
        account1=Account(
            id_=account1_id,
            currency="KZT",
            balance=Decimal(1000)
        )
        account2 = Account(
            id_=account2_id,
            currency="KZT",
            balance=Decimal(500)
        )
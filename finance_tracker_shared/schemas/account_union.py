from typing import Union, Optional, Literal
from pydantic import BaseModel
from finance_tracker_shared.schemas.accounts_all import AccountAllCreate, AccountAllRead
from finance_tracker_shared.schemas.account_credit import AccountCreditCreate, AccountCreditRead
from finance_tracker_shared.schemas.account_debit import AccountDebitCreate, AccountDebitRead
from finance_tracker_shared.schemas.account_independent import AccountIndependentCreate, AccountIndependentRead

class AccountFullRead(BaseModel):
    account: AccountAllRead
    credit: Optional[AccountCreditRead] = None
    debit: Optional[AccountDebitRead] = None
    independent: Optional[AccountIndependentRead] = None

class AccountCreateCredit(BaseModel):
    account: AccountAllCreate
    subtype: AccountCreditCreate
    account_type: Literal["credit"] = "credit"

class AccountCreateDebit(BaseModel):
    account: AccountAllCreate
    subtype: AccountDebitCreate
    account_type: Literal["debit"] = "debit"

class AccountCreateIndependent(BaseModel):
    account: AccountAllCreate
    subtype: AccountIndependentCreate
    account_type: Literal["independent"] = "independent"

AccountCreateUnion = Union[
    AccountCreateCredit,
    AccountCreateDebit,
    AccountCreateIndependent
]

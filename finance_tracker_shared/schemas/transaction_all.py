from typing import Optional
from datetime import date
from pydantic import BaseModel
from finance_tracker_shared.schemas.enums import TransactionTypeEnum

class TransactionAllBase(BaseModel):
    amount: float
    date: date
    description: Optional[str] = None
    transaction_type: TransactionTypeEnum
    paid: bool = True
    recurring_transaction_id: Optional[int] = None

class TransactionAllCreate(TransactionAllBase):
    pass

class TransactionAllRead(TransactionAllBase):
    id: int

    model_config = {
        "from_attributes": True
    }

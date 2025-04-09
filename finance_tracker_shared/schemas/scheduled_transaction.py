from typing import Optional
from datetime import date
from pydantic import BaseModel, field_validator
from finance_tracker_shared.schemas.enums import TransactionTypeEnum

class ScheduledTransactionBase(BaseModel):
    transaction_type: TransactionTypeEnum
    recurring_transaction_id: int
    amount: float
    description: Optional[str] = None
    scheduled_date: date
    pending: bool = True

    folio_id: Optional[int] = None
    to_account_id: Optional[int] = None
    from_account_id: Optional[int] = None
    transaction_id: Optional[int] = None

    @field_validator("amount")
    def validate_amount(cls, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        return amount
    
    @field_validator("description")
    def validate_description(cls, description: Optional[str]) -> Optional[str]:
        if description:
            if len(description) > 50:
                raise ValueError("Description must not exceed 50 characters")
        return description

class ScheduledTransactionCreate(ScheduledTransactionBase):
    pass

class ScheduledTransactionRead(ScheduledTransactionBase):
    id: int

    model_config = {
        "from_attributes": True
    }

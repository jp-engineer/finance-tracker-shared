from pydantic import BaseModel, field_validator

class AccountCreditBase(BaseModel):
    credit_limit: float
    interest_rate: float
    minimum_payment_pct: float
    due_date: int

    @field_validator("due_date")
    def validate_due_date(cls, v):
        if not (1 <= v <= 31):
            raise ValueError("Due date must be between 1 and 31")
        return v

class AccountCreditCreate(AccountCreditBase):
    pass

class AccountCreditRead(AccountCreditBase):
    id: int
    account_id: int

    model_config = {
        "from_attributes": True
    }

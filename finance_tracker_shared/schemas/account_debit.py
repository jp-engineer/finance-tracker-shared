from pydantic import BaseModel, field_validator

class AccountDebitBase(BaseModel):
    overdraft_limit: float
    interest_rate: float

    @field_validator("overdraft_limit")
    def validate_overdraft_limit(cls, v):
        if v < 0:
            raise ValueError("Overdraft limit cannot be negative")
        return v

class AccountDebitCreate(AccountDebitBase):
    pass

class AccountDebitRead(AccountDebitBase):
    id: int
    account_id: int

    model_config = {
        "from_attributes": True
    }

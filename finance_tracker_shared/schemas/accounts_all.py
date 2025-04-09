from pydantic import BaseModel, Field, field_validator
import pycountry
from finance_tracker_shared.schemas.enums import AccountTypeEnum

class AccountAllBase(BaseModel):
    reference: str
    currency: str = Field(default="GBP")
    starting_balance: float
    active: bool = True
    account_type: AccountTypeEnum

    @field_validator("reference")
    def validate_reference(cls, v):
        if not v.strip():
            raise ValueError("Reference cannot be empty")
        if len(v) > 50:
            raise ValueError("Reference cannot exceed 50 characters")
        return v.strip()

    @field_validator("currency")
    def validate_currency_code(cls, v):
        if not pycountry.currencies.get(alpha_3=v.upper()):
            raise ValueError(f"Invalid currency code: {v}")
        return v.upper()

class AccountAllCreate(AccountAllBase):
    pass

class AccountAllRead(AccountAllBase):
    id: int

    model_config = {
        "from_attributes": True
    }

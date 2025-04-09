from typing import Optional
from datetime import date
from pydantic import BaseModel, field_validator
from finance_tracker_shared.schemas.enums import TransactionTypeEnum

DAYS_LONG = {"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"}
DAYS_SHORT = {"mon", "tue", "wed", "thu", "fri", "sat", "sun"}

class RecurringTransactionBase(BaseModel):
    transaction_type: TransactionTypeEnum
    amount: float
    description: str
    variable: bool = False
    estimate: Optional[float] = None

    expires: bool = True
    expires_after: Optional[int] = None
    expires_on: Optional[date] = None

    ignores_bank_holidays: bool = False
    ignores_weekends: bool = False
    pays_early: bool = False

    freq_per_week: Optional[int] = None
    freq_per_month: Optional[int] = None
    freq_per_year: Optional[int] = None

    week_payment_days: Optional[str] = None
    month_payment_days: Optional[str] = None
    month_payment_dates: Optional[str] = None
    year_payment_dates: Optional[str] = None

    folio_id: Optional[int] = None
    to_account_id: Optional[int] = None
    from_account_id: Optional[int] = None

    @field_validator("amount")
    def validate_amount(cls, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        return amount

    @field_validator("description")
    def validate_description(cls, description: str) -> str:
        if description and not description.strip():
            raise ValueError("Description cannot be empty")
        if len(description) > 50:
            raise ValueError("Description must not exceed 50 characters")
        return description
    
    @field_validator("freq_per_week")
    def validate_freq_per_week(cls, freq_per_week: Optional[int]) -> Optional[int]:
        if freq_per_week is not None:
            if freq_per_week < 1 or freq_per_week > 7:
                raise ValueError("Frequency per week must be between 1 and 7")
        return freq_per_week
    
    @field_validator("freq_per_month")
    def validate_freq_per_month(cls, freq_per_month: Optional[int]) -> Optional[int]:
        if freq_per_month is not None:
            if freq_per_month < 1 or freq_per_month > 31:
                raise ValueError("Frequency per month must be between 1 and 31")
        return freq_per_month
    
    @field_validator("freq_per_year")
    def validate_freq_per_year(cls, freq_per_year: Optional[int]) -> Optional[int]:
        if freq_per_year is not None:
            if freq_per_year < 1 or freq_per_year > 365:
                raise ValueError("Frequency per year must be between 1 and 365")
        return freq_per_year

class RecurringTransactionCreate(RecurringTransactionBase):
    pass

class RecurringTransactionRead(RecurringTransactionBase):
    id: int

    model_config = {
        "from_attributes": True
    }

from typing import Any
from pydantic import BaseModel, field_validator, model_validator, computed_field

KEYS = ["date_format", "user_name", "week_starts_on"]

DATE_FORMATS = ["dd-mm-yyyy", "mm-dd-yyyy", "yyyy-mm-dd"]
DAYS_LONG = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAYS_SHORT = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

class SettingViewBase(BaseModel):
    key: str
    value: str

    @computed_field
    @property
    def norm_key(self) -> str:
        return self.key.replace("_", " ").capitalize()

    @field_validator("key")
    def validate_key(cls, key: str) -> str:
        if not key or key not in KEYS:
            raise ValueError(f"Key must be one of {KEYS}")
        return key

    @field_validator("value")
    def validate_value(cls, value: str) -> str:
        if not value or len(value) > 20:
            raise ValueError("Value cannot be empty and must not exceed 20 characters")
        return value

    @model_validator(mode="after")
    def validate_combination(self) -> "SettingViewBase":
        key = self.key
        value = self.value
        
        if key == "date_format":
            if value.lower() not in DATE_FORMATS:
                raise ValueError(f"Invalid date format: {value}")
            else:
                self.value = value.upper()
            
        elif key == "user_name":
            special_chars = ["!", "@", "#", "$", "%", "^", "*", "(", ")", "=", "+", "{", "}", "[", "]", ";", ":", "'", '"', "<", ">", ",", ".", "?", "/", "|", "\\"]
            if any(char in value for char in special_chars):
                raise ValueError("User name cannot contain special characters")
            elif len(value) < 3:
                raise ValueError("User name must be at least 3 characters long")
            elif len(value) > 20:
                raise ValueError("User name must not exceed 20 characters")
            else:
                self.value = value.title()

        elif key == "week_starts_on":
            if value.lower() not in DAYS_LONG and value.lower() not in DAYS_SHORT:
                raise ValueError(f"Invalid week start day: {value}")
            else:
                if value in DAYS_SHORT:
                    value = DAYS_LONG[DAYS_SHORT.index(value)]
                self.value = value.capitalize()

        return self

class SettingViewCreate(SettingViewBase):
    pass

class SettingViewRead(SettingViewBase):
    id: int

    model_config = {
        "from_attributes": True
    }

class SettingViewUpdate(BaseModel):
    key: str
    value: Any

    @model_validator(mode="before")
    @classmethod
    def validate_with_key(cls, data: dict) -> dict:
        key = data.get("key")
        value = data.get("value")

        if key is None:
            raise ValueError("Key must be provided for validation")

        validated = SettingViewBase(key=key, value=value)

        return {
            "key": validated.key,
            "value": validated.value
        }

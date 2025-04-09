from typing import Any
from datetime import datetime
from pydantic import BaseModel, field_validator, model_validator, computed_field

KEYS = ["start_date"]

class SettingDeveloperBase(BaseModel):
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
    def validate_combination(self) -> "SettingDeveloperBase":
        key = self.key
        value = self.value

        if key == "start_date":
            try:
                datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                raise ValueError(f"Invalid start_date: {value}. Expected format: yyyy-mm-dd")

        return self

class SettingDeveloperCreate(SettingDeveloperBase):
    pass

class SettingDeveloperRead(SettingDeveloperBase):
    id: int

    model_config = {
        "from_attributes": True
    }

class SettingDeveloperUpdate(BaseModel):
    key: str
    value: Any

    @model_validator(mode="before")
    @classmethod
    def validate_with_key(cls, data: dict) -> dict:
        key = data.get("key")
        value = data.get("value")

        if key is None:
            raise ValueError("Key must be provided for validation")

        validated = SettingDeveloperBase(key=key, value=value)

        return {
            "key": validated.key,
            "value": validated.value
        }

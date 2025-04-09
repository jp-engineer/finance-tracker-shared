from pydantic import BaseModel, field_validator
from finance_tracker_shared.schemas.enums import FolioCategoryEnum

class FolioBase(BaseModel):
    name: str
    category: FolioCategoryEnum
    subcategory: str

    @field_validator("name")
    def validate_name(cls, name: str) -> str:
        if not name or len(name) > 50:
            raise ValueError("Name cannot be empty and must not exceed 50 characters")
        return name
    
    @field_validator("category")
    def validate_category(cls, category: FolioCategoryEnum) -> FolioCategoryEnum:
        if not category:
            raise ValueError("Category cannot be empty")
        return category
    
    @field_validator("subcategory")
    def validate_subcategory(cls, subcategory: str) -> str:
        if len(subcategory) > 50:
            raise ValueError("Subcategory cannot exceed 50 characters")
        return subcategory

class FolioCreate(FolioBase):
    pass

class FolioRead(FolioBase):
    model_config = {
        "from_attributes": True
    }

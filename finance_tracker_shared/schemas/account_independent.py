from pydantic import BaseModel

class AccountIndependentBase(BaseModel):
    pass

class AccountIndependentCreate(BaseModel):
    pass

class AccountIndependentRead(BaseModel):
    id: int
    account_id: int

    model_config = {
        "from_attributes": True
    }

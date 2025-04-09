from pydantic import BaseModel

class TransactionExpenseBase(BaseModel):
    from_account_id: int
    folio_id: int

class TransactionExpenseCreate(TransactionExpenseBase):
    pass

class TransactionExpenseRead(TransactionExpenseBase):
    id: int
    transaction_id: int

    model_config = {
        "from_attributes": True
    }

from pydantic import BaseModel

class TransactionPaymentBase(BaseModel):
    to_account_id: int
    folio_id: int

class TransactionPaymentCreate(TransactionPaymentBase):
    pass

class TransactionPaymentRead(TransactionPaymentBase):
    id: int
    transaction_id: int

    model_config = {
        "from_attributes": True
    }

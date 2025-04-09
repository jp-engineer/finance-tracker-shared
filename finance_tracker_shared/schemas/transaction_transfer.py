from pydantic import BaseModel

class TransactionTransferBase(BaseModel):
    from_account_id: int
    to_account_id: int

class TransactionTransferCreate(TransactionTransferBase):
    pass

class TransactionTransferRead(TransactionTransferBase):
    id: int
    transaction_id: int

    model_config = {
        "from_attributes": True
    }

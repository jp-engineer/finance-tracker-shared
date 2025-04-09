from typing import Optional, Union, Literal
from pydantic import BaseModel
from finance_tracker_shared.schemas.transaction_all import TransactionAllCreate, TransactionAllRead
from finance_tracker_shared.schemas.transaction_payment import TransactionPaymentCreate, TransactionPaymentRead
from finance_tracker_shared.schemas.transaction_expense import TransactionExpenseCreate, TransactionExpenseRead
from finance_tracker_shared.schemas.transaction_transfer import TransactionTransferCreate, TransactionTransferRead

class TransactionFullRead(BaseModel):
    transaction: TransactionAllRead
    payment: Optional[TransactionPaymentRead] = None
    expense: Optional[TransactionExpenseRead] = None
    transfer: Optional[TransactionTransferRead] = None

class TransactionCreatePayment(BaseModel):
    transaction: TransactionAllCreate
    subtype: TransactionPaymentCreate
    transaction_type: Literal["payment"] = "payment"

class TransactionCreateExpense(BaseModel):
    transaction: TransactionAllCreate
    subtype: TransactionExpenseCreate
    transaction_type: Literal["expense"] = "expense"

class TransactionCreateTransfer(BaseModel):
    transaction: TransactionAllCreate
    subtype: TransactionTransferCreate
    transaction_type: Literal["transfer"] = "transfer"

TransactionCreateUnion = Union[
    TransactionCreatePayment,
    TransactionCreateExpense,
    TransactionCreateTransfer
]

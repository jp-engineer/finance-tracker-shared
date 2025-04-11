from typing import Optional, Any
from pydantic import BaseModel

class APIResponse(BaseModel):
    message: Optional[str] = None
    data: Optional[Any] = None

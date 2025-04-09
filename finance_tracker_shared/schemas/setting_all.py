from pydantic import BaseModel
from typing import Optional, List
from finance_tracker_shared.schemas import SettingGeneralBase, SettingViewBase, SettingDeveloperBase

class SettingAllUpdatePayload(BaseModel):
    general: Optional[List[SettingGeneralBase]] = []
    view: Optional[List[SettingViewBase]] = []
    developer: Optional[List[SettingDeveloperBase]] = []

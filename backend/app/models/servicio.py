from typing import Optional

from pydantic import BaseModel

from datetime import datetime


class Servicio(BaseModel):
    id: Optional[int]
    service_name: str
    unit_cost: int
    category_service: str

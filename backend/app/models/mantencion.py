from typing import Optional

from pydantic import BaseModel

from datetime import datetime


class Mantencion(BaseModel):
    id: Optional[int]
    id_auto: int
    id_servicio: int
    fecha_servicio: datetime = datetime.now()

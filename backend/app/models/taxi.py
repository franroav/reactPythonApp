from typing import Optional

from pydantic import BaseModel


class Taxi(BaseModel):
    id: Optional[int]
    modelo: str
    ano: int
    marca: str
    km: int
    oil_tank: int
    gasoline_tank: int
    presion: int

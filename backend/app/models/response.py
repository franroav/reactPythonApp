from typing import Optional, List, Text, Dict

from pydantic import BaseModel

from datetime import datetime


class serviceResponse(BaseModel):
    title: str
    statusCode: int
    payload: List


class Response(BaseModel):
    statusCode: int
    data: Dict

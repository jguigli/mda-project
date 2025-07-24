from pydantic import BaseModel
from datetime import date, time

class Log(BaseModel):
    timestamp: str
    level: str
    message: str
    service: str

class SearchedLogs(BaseModel):
    q: str
    level: str
    service: str
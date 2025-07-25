from pydantic import BaseModel

class Log(BaseModel):
    timestamp: str
    level: str
    message: str
    service: str
from pydantic import BaseModel
from enum import Enum

# validation si level dans le schema Log est une des 4 valeurs suivantes
class levelEnum(str, Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    DEBUG = "DEBUG"

class Log(BaseModel):
    timestamp: str
    level: levelEnum
    message: str
    service: str


import enum
from typing import Dict, List

from pydantic import BaseModel


class MessageRole(enum.Enum):
    ASSISTANT = "assistant"
    USER = "user"


class Message(BaseModel):
    role: MessageRole
    content: List[Dict[str, str]]

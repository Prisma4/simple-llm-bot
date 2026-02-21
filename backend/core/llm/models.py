import enum
from typing import Dict, List, Union

from pydantic import BaseModel


class MessageRole(enum.Enum):
    ASSISTANT = "assistant"
    USER = "user"


class Message(BaseModel):
    role: MessageRole
    content: List[Dict[str, Union[str, dict]]]

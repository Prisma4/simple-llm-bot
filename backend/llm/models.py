import enum

from pydantic import BaseModel


class MessageRole(enum.Enum):
    ASSISTANT = "assistant"
    USER = "user"


class Message(BaseModel):
    role: MessageRole
    content: str

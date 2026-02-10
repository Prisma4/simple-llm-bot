import json
from typing import Optional, List
import redis.asyncio as redis

from core.context_manager.base import AbstractMessageContextManager
from core.llm.models import Message


class RedisMessageContextManager(AbstractMessageContextManager):
    _redis = None

    def __init__(
        self,
        redis_url: str = "redis://localhost:6379/0",
        prefix: str = "chat_context",
        max_history_length: int = 50,
        ttl_seconds: Optional[int] = 604800,
    ):
        self.prefix = prefix
        self.max_history_length = max_history_length
        self.ttl = ttl_seconds

        if RedisMessageContextManager._redis is None:
            RedisMessageContextManager._redis = redis.from_url(
                redis_url,
                decode_responses=False,
            )

        self.redis = RedisMessageContextManager._redis

    def _get_key(self, user_id: str) -> str:
        return f"{self.prefix}:{user_id}"

    async def save_message(self, key: str, message: Message) -> None:
        redis_key = self._get_key(key)
        message_dict = message.model_dump(mode="json", exclude_none=True)
        await self.redis.rpush(redis_key, json.dumps(message_dict))
        if self.max_history_length:
            await self.redis.ltrim(redis_key, -self.max_history_length, -1)
        if self.ttl:
            await self.redis.expire(redis_key, self.ttl)

    async def get_context(self, key: str) -> List[Message]:
        redis_key = self._get_key(key)
        raw_messages = await self.redis.lrange(redis_key, 0, -1)
        messages = []
        for raw in raw_messages:
            try:
                data = json.loads(raw)
                msg = Message.model_validate(data)
                messages.append(msg)
            except Exception:
                continue
        return messages

    async def clear_context(self, key: str) -> None:
        redis_key = self._get_key(key)
        await self.redis.delete(redis_key)

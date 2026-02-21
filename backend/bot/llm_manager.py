from core.context_manager.redis_context import RedisMessageContextManager
from core.llm.llm_interface.open_ai import OpenAILLMInterface
from core.llm_manager.manager import LLMManager
from settings import Settings

settings = Settings()

llm_manager = LLMManager(
    context_manager=RedisMessageContextManager(settings.redis_url),
    llm_interface=OpenAILLMInterface(
        settings.openai_api_key,
        settings.openai_model,
        "Generate MarkdownV2 with escaped _ * [ ] ( ) ~ ` > # + - = | { } . ! in plain text" + settings.system_prompt,
    )
)

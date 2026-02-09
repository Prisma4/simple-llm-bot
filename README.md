# Simple LLM Bot

A Telegram bot that lets you chat with a powerful language model (like ChatGPT).

### Features

- Replies to any text message
- Remembers conversation history
- Can start a fresh conversation (clear history)

### Quick Start

1. Clone the repository

```bash
git clone https://github.com/Prisma4/simple-llm-bot.git
cd simple-llm-bot
```

2. Create a file called `.env` in the root folder and fill it:

```env
BOT_TOKEN=your_telegram_bot_token_here
OPENAI_API_KEY=sk-........................................
OPENAI_MODEL=gpt-3.5-turbo          # or gpt-4o-mini, gpt-4o, etc.
SYSTEM_PROMPT=You are a helpful assistant.
```

3. Run with Docker (easiest way)

```bash
docker compose up --build
```

That’s it — the bot is now online.

### How to use

- Just send any message to the bot → it will reply
- To start a new conversation (forget previous messages) → press the “New Request” button or send the configured command

### Required .env variables

- `BOT_TOKEN`        — Telegram bot token  
- `OPENAI_API_KEY`  — your OpenAI API key  
- `OPENAI_MODEL`    — model name (e.g. gpt-3.5-turbo, gpt-4o-mini)  
- `SYSTEM_PROMPT`   — initial instruction for the model
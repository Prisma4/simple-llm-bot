# Simple LLM Bot

This bot allows users to interact with a large language model (LLM), such as **ChatGPT**. The bot stores user messages, processes them through the LLM, and responds with generated answers.

## Features

- Responds to text messages from users.
- Stores conversation context (user's message history).
- Clears conversation context on request.
- Integrates with ChatGPT API (or other LLMs) for generating responses.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Prisma4/simple-llm-bot.git
cd simple-llm-bot
```

### 2. Create a `.env` file

Create a `.env` file in the root of the project and add the following environment variables:

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-3.5-turbo  # Or gpt-4 if available
OPENAI_API_URL=open_api_url
BOT_TOKEN=your_telegram_bot_api_token  # Telegram bot token
```

Replace `your_openai_api_key` with your actual OpenAI API key, and both `your_telegram_bot_api_token` placeholders with your Telegram Bot API token.

### 3. Build and start the Docker containers

The project uses **Docker Compose**, and the necessary configurations are already provided. To build and start the services, simply run:

```bash
docker-compose up --build
```

This will:
- Build the Docker images.
- Start the bot and any dependent services.
- The bot will be up and running, ready to listen for messages.

### 4. Verify the bot

Send the `/start` command to your bot on Telegram, and begin interacting. The bot should respond to your messages and process them through the connected LLM.

### 5. Clearing the context

To clear the conversation history, send the command defined in your bot's settings (for example, `/clear` or another custom command).

## Environment Variables

Make sure the following environment variables are set in the `.env` file:

| Variable                 | Description                                                 |
|--------------------------|-------------------------------------------------------------|
| `OPENAI_API_KEY`         | Your OpenAI API key (required for ChatGPT API integration). |
| `OPENAI_MODEL`           | The OpenAI model to use, e.g., `gpt-3.5-turbo` or `gpt-4`.  |
| `OPENAI_API_URL`         | OpenAI API url. ( Optional ).                               |
| `BOT_TOKEN`              | Telegram bot token.                                         |

## Notes

- The bot uses **`pydantic`** to handle environment variables, making it easy to manage different configurations.
- The bot stores the user messages and interacts with the LLM to provide contextual responses.
- The code is designed for easy expansion, so you can replace the LLM interface to support different models or services if needed.

---

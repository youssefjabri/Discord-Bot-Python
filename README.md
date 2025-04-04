<img width=400 src="https://github.com/user-attachments/assets/a971b5e9-8f76-41c4-bcfe-a54d5d81cc0f" align="right"/>

# Discord Bot README

## Overview
This repository contains a simple Discord bot written in Python. The bot listens for messages in a Discord server and responds based on predefined responses. It can also handle private messages.

## Features
- Responds to user messages with predefined replies.
- Can distinguish between public and private messages.
- Simple command set including greeting, providing sample Python code, and rolling a dice.

## Prerequisites
- Python 3.12.4 .
- A Discord account & a bot token.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/youssefjabri/Discord-Bot-Python.git
    cd Discord-Bot-Python
    ```

2. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Set up your `.env` file:**

    Create a `.env` file in the root directory of the project and add your Discord bot token:

    ```sh
    DISCORD_TOKEN=your_discord_bot_token_here
    ```

## Usage

1. **Run the bot:**

    ```sh
    python main.py
    ```

2. **Interact with the bot:**

    - Send a message containing "hello" and the bot will respond with "Hello there!"
    - Ask for a simple Python code snippet with "give me a simple code with python" and the bot will provide a basic example.
    - Request a dice roll with "roll dice" and the bot will simulate rolling a dice.
    - The bot will respond with a generic message if it doesn't understand the input.

## Files

- `main.py`: Main script that sets up the Discord bot and handles message events.
- `Responses.py`: Contains logic for generating responses based on user messages.
- `requirements.txt`: Lists the dependencies required for the project.
- `.env`: File containing environment variables, specifically the Discord bot token.

## main.py

This script initializes and runs the Discord bot. It contains the following main sections:

1. **Load environment variables from `.env` file**:
   ```python
   load_dotenv()
   TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
   ```

2. **Configure Discord intents and create the client**:
   ```python
   intents: Intents = Intents.default()
   intents.message_content = True
   client: Client = Client(intents=intents)
   ```

3. **Function to send messages in response to users**:
   ```python
   async def send_message(message: Message, user_message: str) -> None:
   ```

4. **Event triggered when the bot is ready**:
   ```python
   @client.event
   async def on_ready() -> None:
   ```

5. **Event triggered with each new message**:
   ```python
   @client.event
   async def on_message(message: Message) -> None:
   ```

6. **Run the bot**:
   ```python
   def main() -> None:
       client.run(TOKEN)
   
   if __name__ == '__main__':
       main()
   ```

## Responses.py

This script contains the `get_response` function which processes user input and returns appropriate responses.

```python
from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    if lowered == '':
        return "Well you're awfully silent"
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'give me a simple code with python' in lowered:
        return '`print("Hello World!")`'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return choice([
            "I don't understand",
            "What are you talking about?",
        ])
```

## requirements.txt

Lists the dependencies required for the project:

```
python-dotenv
discord
```

## .env File

Stores the Discord bot token:

```
DISCORD_TOKEN=your_discord_bot_token_here
```

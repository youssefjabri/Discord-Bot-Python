from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from Responses import get_response

#1 Load environment variables from .env file
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

#2 Configuring Discord Intents & Creating the Client
intents: Intents = Intents.default()
intents.message_content = True  # Enable access to message content
client: Client = Client(intents=intents)

#3 Function to send messages in response to users
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(message was empty because intents were not enabled probably)')
        return

    # Check if the message is private
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        # Get a response based on the user's message
        response: str = get_response(user_message)
        # Send the response as a private message or on the public channel
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

#4 Event that triggers when the bot is ready
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running')

#5 Event that triggers with each new message
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    # Show message details for debugging
    print(f'[{channel}] {username} : "{user_message}"')
    
    await send_message(message, user_message)

#6 Run the bot
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
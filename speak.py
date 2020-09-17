import os
import random

import discord
from dotenv import load_dotenv

from token_cc import token  # to protect the token ofcourse

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    res_quotes = [
        'Hello', 'Speak!', 'Test', 'What do you want?'
    ]

    if message.content == 'Speak!':
        response = random.choice(res_quotes)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException


client.run(token(), bot=True)

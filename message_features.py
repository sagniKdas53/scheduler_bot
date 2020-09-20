import discord

import bot_friendly
from token_cc import token

client = discord.Client()
bot_friendly.main()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_ready():
    for guild in client.guilds:
        print(guild.name)
        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("&&send"):
        text = message.content
        text = text.split(' ')
        # print(text) show_by_name('Fubuki', 'Asia/Kolkata','show_all'))
        name = text[1]
        time = text[2]
        stat = text[3]
        response = bot_friendly.show_by_name(name, time, stat)
        await message.channel.send(response)
    if message.content.startswith("&&exit"):
        await message.channel.send("Exiting")
        await client.close()
        print("Successfully logged out")
    elif message.content == 'raise-exception':
        raise discord.DiscordException


@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


client.run(token(), bot=True)

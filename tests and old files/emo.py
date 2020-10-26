import discord

from token_cc import token

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        print(guild.name)
        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')

    for emo_g in client.emojis:
        print(emo_g.name)
        print(emo_g.id)
        print(emo_g.require_colons)


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    print(message.content)


client.run(token(), bot=True)

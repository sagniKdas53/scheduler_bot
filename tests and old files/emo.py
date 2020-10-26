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
        if emo_g.require_colons:
            print('<:' + emo_g.name + ':' + emo_g.id + '>')
        else:
            print('<:' + emo_g.name + ':' + emo_g.id + '>')


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if ':8036_Ahegao:' in message.content:
        await message.add_reaction(emoji=client.emojis[0])
    print(message.content)


client.run(token(), bot=True)

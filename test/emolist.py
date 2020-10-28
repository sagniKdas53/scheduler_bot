import discord

from token_cc import token

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    for guild in client.guilds:
        print(f'{client.user} is connected to the following guild:\n'f'{guild.name}(id: {guild.id})')

    for emo_g in client.emojis:
        print(emo_g.name, emo_g.guild, emo_g.id, emo_g.guild_id)
    await client.close()


client.run(token(), bot=True)

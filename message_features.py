import discord

import bot_friendly
from token_cc import token

client = discord.Client()
obJ_class = bot_friendly.ExecFaster()


# global obJ_class


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
    # global obJ_class
    if message.author == client.user:
        return
    if message.content.startswith("&&send"):
        text = message.content
        text = text.split(' ')
        name = text[1]
        time = text[2]
        stat = text[3]
        link_s, response = obJ_class.show_by_name(name, time, stat)
        embed = discord.Embed(title='Links')
        for row in range(0, len(link_s)):
            embed.add_field(name='[' + str(row) + ']', value=link_s[row])
        # await message.channel.send(embed=embed)
        '''
        New Idea: send the normal stuff and then send the link in embeds.
        '''
        await message.channel.send(response)
        await message.channel.send(embed=embed)
    if message.content.startswith("&&exit"):
        await message.channel.send("Exiting")
        await client.close()
        print("Successfully logged out")
    if message.content.startswith("&&update"):
        await message.channel.send("Wait a few seconds")
        # obJ_class = bot_friendly.ExecFaster()
        obJ_class.update()
        '''
        The idea was to reassign the object to itself to make a global upgraded copy
        global obJ_class
        obJ_class = bot_friendly.ExecFaster()
        del obJ_class
        obJ_class = obJ_class_
        '''
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

import asyncio

import discord

from token_cc import token

client = discord.Client()
dict_emo = {}
dict_rem = {'https://www.youtube.com/watch?v=JVovZkcU5tk': 360, 'https://www.youtube.com/watch?v=ILS8ITPBCz0': 299,
            'https://youtu.be/5EXFilTUiko?list=RD5EXFilTUiko': 720}
link_s = ['https://youtu.be/5EXFilTUiko?list=RD5EXFilTUiko', 'https://www.youtube.com/watch?v=ILS8ITPBCz0',
          'https://www.youtube.com/watch?v=JVovZkcU5tk']


@client.event
async def on_ready():
    for guild in client.guilds:
        print(guild.name)
        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')

    for emo_g in client.emojis:
        dict_emo[emo_g.name] = emo_g
        if emo_g.require_colons:
            print('<:' + emo_g.name + ':' + str(emo_g.id) + '>')
        else:
            print('<:' + emo_g.name + ':' + str(emo_g.id) + '>')


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if ':8036_Ahegao:' in message.content:
        await message.add_reaction(emoji=dict_emo['8036_Ahegao'])
    print(message.content)
    if message.content.startswith("&&send"):
        resp = await message.channel.send('Add a reaction in 30 sec to set reminder')
        '''
        firstly, make a way to check if there are any reminder worthy streams in the list if there are then add reacts,
        also figure out a way to actually send the messages at the given time.
        '''
        await resp.add_reaction(emoji=dict_emo['keycap1'])
        await resp.add_reaction(emoji=dict_emo['keycap2'])
        await resp.add_reaction(emoji=dict_emo['keycap3'])

        def check(ree, ur):
            em = str(ree.emoji)
            print('in check ', em, ' react from ', ur)
            if message.author == ur:
                if em == '<:keycap1:770320921113264158>' or em == '<:keycap2:770321327193718824>' \
                        or em == '<:keycap3:770321274110083072>':
                    return True
            return False

        async def rem(choice):
            print(choice)
            await asyncio.sleep(dict_rem[link_s[choice]] - 300)
            await message.author.send(link_s[choice])

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
            print('Got ', reaction, ' from ', user)
            '''Need to format the messages test if the async io can handle long waits like days without becoming 
            unstable and check if emo actually getting the right string or do i need to use str(reaction.emoji.name)'''
            emo = reaction.emoji
            print('emo =', emo, '\n Type of emo is= ', type(emo), '\ntype of dict var is=',
                  type(dict_emo[str(emo.name)]), '\n The queried emoji is= ', dict_emo[str(emo.name)],
                  '\n The emoji key is=', str(emo.name))
            try:
                if emo == dict_emo['keycap1']:
                    await rem(0)
                if emo == dict_emo['keycap2']:
                    await rem(1)
                if emo == dict_emo['keycap3']:
                    await rem(2)

            except (asyncio.TimeoutError, TypeError):
                pass
        except asyncio.TimeoutError:
            await message.channel.send('Failed to react')
        else:
            await message.channel.send('React got')


client.run(token(), bot=True)

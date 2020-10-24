import asyncio

import discord

from token_cc import token

client = discord.Client()
times = [60, 120, 30]


@client.event
async def on_message(message):
    user = message.author
    channel = message.channel
    if user == client.user:
        return
    if message.content.startswith("&&send"):
        resp = await channel.send("react in 30 seconds")
        await resp.add_reaction(u"\U0001F446")
        await resp.add_reaction(u"\U0001F44A")
        await resp.add_reaction(u"\U0001F447")

        def check(ree, ur):
            em = str(ree.emoji)
            if message.author == ur:
                if em == u"\U0001F446" or em == u"\U0001F44A" or em == u"\U0001F447":
                    return True
            return False

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
            print('Got ', reaction, ' from ', user)
            emo = str(reaction.emoji)
            if emo == u"\U0001F446":
                await asyncio.sleep(times[0])
                await user.send(u"\U0001F446" + " is  = " + str(times[0]))
            if emo == u"\U0001F44A":
                await asyncio.sleep(times[1])
                await user.send(u"\U0001F44A" + " is  = " + str(times[1]))
            if emo == u"\U0001F447":
                await asyncio.sleep(times[2])
                await user.send(u"\U0001F447" + " is  = " + str(times[2]))
        except asyncio.TimeoutError:
            await channel.send('Failed to react')

    if message.content.startswith("&&exit"):
        await channel.send("Exiting")
        await client.close()
        print("Successfully logged out")


client.run(token(), bot=True)

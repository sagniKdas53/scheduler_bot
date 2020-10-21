import asyncio

import discord

from token_cc import token

client = discord.Client()


@client.event
async def on_message(message):
    user = message.author
    chael = message.channel
    if user == client.user:
        return
    if message.content.startswith("&&send"):
        resp = await chael.send("👩‍🎤🦵🤯")
        embed = discord.Embed(title='Reacts')
        embed.add_field(name="HAACHAMA", value="heh",
                        inline=True)
        embed.set_image(url='https://i.imgur.com/kThPzF9.jpeg')
        await chael.send(embed=embed)
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
                await chael.send("ONE")
            if emo == u"\U0001F44A":
                await chael.send("TWO")
            if emo == u"\U0001F447":
                await chael.send("THREE")
        except asyncio.TimeoutError:
            await chael.send('Failed to react')
        else:
            await chael.send('React got')

    if message.content.startswith("&&exit"):
        await chael.send("Exiting")
        await client.close()
        print("Successfully logged out")


client.run(token(), bot=True)

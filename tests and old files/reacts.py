import discord

from token_cc import token

client = discord.Client()


@client.event
async def on_message(message):
    user = message.author
    if user == client.user:
        return
    if message.content.startswith("&&send"):
        resp = await message.channel.send("👩‍🎤🦵🤯")
        embed = discord.Embed(title='Reacts')
        embed.add_field(name="HAACHAMA", value="heh",
                        inline=True)
        embed.set_image(url='https://i.imgur.com/kThPzF9.jpeg')
        await message.channel.send(embed=embed)
        embed.clear_fields()
        await resp.add_reaction(u"\U0001F446")
        await resp.add_reaction(u"\U0001F44A")
        await resp.add_reaction(u"\U0001F447")

    if message.content.startswith("&&exit"):
        await message.channel.send("Exiting")
        await client.close()
        print("Successfully logged out")


@client.event
async def on_reaction_add(reaction, user):
    emoji = reaction.emoji

    if user == client.user:
        return

    if emoji == u"\U0001F446":
        print("ONE")
    elif emoji == u"\U0001F44A":
        # do stuff
        print('TWO')
    elif emoji == u"\U0001F447":
        # do stuff
        print('THREE')
    else:
        return


client.run(token(), bot=True)
